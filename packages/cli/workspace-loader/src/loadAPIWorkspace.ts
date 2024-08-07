import { ASYNCAPI_DIRECTORY, generatorsYml, OPENAPI_DIRECTORY } from "@fern-api/configuration";
import { AbsoluteFilePath, doesPathExist, join, RelativeFilePath } from "@fern-api/fs-utils";
import { TaskContext } from "@fern-api/task-context";
import { loadAPIChangelog } from "./loadAPIChangelog";
import { getValidAbsolutePathToAsyncAPIFromFolder } from "./loadAsyncAPIFile";
import { getValidAbsolutePathToOpenAPIFromFolder } from "./loadOpenAPIFile";
import { ProtobufOpenAPIGenerator } from "./protobuf/ProtobufOpenAPIGenerator";
import { WorkspaceLoader, WorkspaceLoaderFailureType } from "./types/Result";
import { APIChangelog, Spec } from "./types/Workspace";
import { OSSWorkspace } from "./workspaces";
import { LazyFernWorkspace } from "./workspaces/FernWorkspace";

export async function loadAPIWorkspace({
    absolutePathToWorkspace,
    context,
    cliVersion,
    workspaceName
}: {
    absolutePathToWorkspace: AbsoluteFilePath;
    context: TaskContext;
    cliVersion: string;
    workspaceName: string | undefined;
}): Promise<WorkspaceLoader.Result> {
    const generatorsConfiguration = await generatorsYml.loadGeneratorsConfiguration({
        absolutePathToWorkspace,
        context
    });

    let changelog: APIChangelog | undefined = undefined;
    try {
        changelog = await loadAPIChangelog({ absolutePathToWorkspace });
    } catch (err) {}

    const absolutePathToOpenAPIFolder = join(absolutePathToWorkspace, RelativeFilePath.of(OPENAPI_DIRECTORY));
    const openApiDirectoryExists = await doesPathExist(absolutePathToOpenAPIFolder);

    const absolutePathToAsyncAPIFolder = join(absolutePathToWorkspace, RelativeFilePath.of(ASYNCAPI_DIRECTORY));
    const asyncApiDirectoryExists = await doesPathExist(absolutePathToAsyncAPIFolder);

    const protobufOpenAPIGenerator = new ProtobufOpenAPIGenerator({
        context,
        absolutePathToWorkspace
    });

    if (generatorsConfiguration?.api != null && generatorsConfiguration.api.definitions.length > 0) {
        const specs: Spec[] = [];

        for (const definition of generatorsConfiguration.api.definitions) {
            const absoluteFilepathToOverrides =
                definition.overrides != null
                    ? join(absolutePathToWorkspace, RelativeFilePath.of(definition.overrides))
                    : undefined;
            if (definition.schema.type === "protobuf") {
                const openAPIAbsoluteFilePath = await protobufOpenAPIGenerator.generate({
                    apiDefinition: definition.schema,
                    local: definition.schema.localGeneration
                });
                specs.push({
                    absoluteFilepath: openAPIAbsoluteFilePath,
                    absoluteFilepathToOverrides,
                    settings: {
                        audiences: definition.audiences ?? [],
                        shouldUseTitleAsName: definition.settings?.shouldUseTitleAsName ?? true,
                        shouldUseUndiscriminatedUnionsWithLiterals:
                            definition.settings?.shouldUseUndiscriminatedUnionsWithLiterals ?? false
                    }
                });
                continue;
            }
            const absoluteFilepath = join(absolutePathToWorkspace, RelativeFilePath.of(definition.schema.path));
            if (!(await doesPathExist(absoluteFilepath))) {
                return {
                    didSucceed: false,
                    failures: {
                        [RelativeFilePath.of(definition.schema.path)]: {
                            type: WorkspaceLoaderFailureType.FILE_MISSING
                        }
                    }
                };
            }
            if (
                definition.overrides != null &&
                absoluteFilepathToOverrides != null &&
                !(await doesPathExist(absoluteFilepathToOverrides))
            ) {
                return {
                    didSucceed: false,
                    failures: {
                        [RelativeFilePath.of(definition.overrides)]: {
                            type: WorkspaceLoaderFailureType.FILE_MISSING
                        }
                    }
                };
            }
            specs.push({
                absoluteFilepath,
                absoluteFilepathToOverrides,
                settings: {
                    audiences: definition.audiences ?? [],
                    shouldUseTitleAsName: definition.settings?.shouldUseTitleAsName ?? true,
                    shouldUseUndiscriminatedUnionsWithLiterals:
                        definition.settings?.shouldUseUndiscriminatedUnionsWithLiterals ?? false
                }
            });
        }
        return {
            didSucceed: true,
            workspace: new OSSWorkspace({
                specs,
                workspaceName,
                absoluteFilepath: absolutePathToWorkspace,
                generatorsConfiguration,
                changelog
            })
        };
    }

    if (openApiDirectoryExists) {
        const absolutePathToAsyncAPI = asyncApiDirectoryExists
            ? await getValidAbsolutePathToAsyncAPIFromFolder(context, absolutePathToAsyncAPIFolder)
            : undefined;
        const absolutePathToOpenAPI = await getValidAbsolutePathToOpenAPIFromFolder(
            context,
            absolutePathToOpenAPIFolder
        );
        const specs: Spec[] = [];
        if (absolutePathToOpenAPI != null) {
            specs.push({
                absoluteFilepath: absolutePathToOpenAPI,
                absoluteFilepathToOverrides: undefined
            });
        }
        if (absolutePathToAsyncAPI != null) {
            specs.push({
                absoluteFilepath: absolutePathToAsyncAPI,
                absoluteFilepathToOverrides: undefined
            });
        }
        if (absolutePathToOpenAPI != null && absolutePathToAsyncAPI != null) {
            return {
                didSucceed: false,
                failures: {
                    [RelativeFilePath.of("openapi/openapi.yml")]: {
                        type: WorkspaceLoaderFailureType.FILE_MISSING
                    }
                }
            };
        }
        return {
            didSucceed: true,
            workspace: new OSSWorkspace({
                specs,
                workspaceName,
                absoluteFilepath: absolutePathToWorkspace,
                generatorsConfiguration,
                changelog
            })
        };
    }

    const fernWorkspace = new LazyFernWorkspace({
        absoluteFilepath: absolutePathToWorkspace,
        generatorsConfiguration,
        workspaceName,
        changelog,
        context,
        cliVersion
    });

    return {
        didSucceed: true,
        workspace: fernWorkspace
    };
}
