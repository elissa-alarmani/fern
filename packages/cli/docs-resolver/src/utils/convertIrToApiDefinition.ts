import {
    APIV1Read,
    DocsV1Read,
    convertAPIDefinitionToDb,
    convertDbAPIDefinitionToRead,
    SDKSnippetHolder
} from "@fern-api/fdr-sdk";
import { IntermediateRepresentation } from "@fern-api/ir-sdk";
import { convertIrToFdrApi } from "@fern-api/register";

const EMPTY_SNIPPET_HOLDER = new SDKSnippetHolder({
    snippetsBySdkId: {},
    snippetsConfigWithSdkId: {},
    snippetTemplatesByEndpoint: {},
    snippetsBySdkIdAndEndpointId: {},
    snippetTemplatesByEndpointId: {}
});

export function convertIrToApiDefinition(
    ir: IntermediateRepresentation,
    apiDefinitionId: string,
    playgroundConfig?: DocsV1Read.PlaygroundConfig
): APIV1Read.ApiDefinition {
    // the navigation constructor doesn't need to know about snippets, so we can pass an empty object
    return convertDbAPIDefinitionToRead(
        convertAPIDefinitionToDb(
            convertIrToFdrApi({ ir, snippetsConfig: {}, playgroundConfig }),
            apiDefinitionId,
            EMPTY_SNIPPET_HOLDER
        )
    );
}
