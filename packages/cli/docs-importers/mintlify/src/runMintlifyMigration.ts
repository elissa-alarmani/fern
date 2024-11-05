import { FERN_DIRECTORY, PROJECT_CONFIG_FILENAME } from "@fern-api/configuration";
import { FernDocsBuilderImpl } from "@fern-api/docs-importer-commons";
import { AbsoluteFilePath, join, RelativeFilePath } from "@fern-api/fs-utils";
import { CONSOLE_LOGGER } from "@fern-api/logger";
import { createMockTaskContext } from "@fern-api/task-context";
import { writeFile } from "fs/promises";
import { MintlifyImporter } from "./MintlifyImporter";

interface RunMintlifyMigrationParams {
    absolutePathToMintJson: AbsoluteFilePath;
    outputPath: AbsoluteFilePath;
}

export async function runMintlifyMigration({
    absolutePathToMintJson,
    outputPath
}: RunMintlifyMigrationParams): Promise<void> {
    const context = createMockTaskContext({ logger: CONSOLE_LOGGER });

    const mintlifyImporter = new MintlifyImporter({
        context
    });

    const builder = new FernDocsBuilderImpl();

    await mintlifyImporter.import({
        args: { absolutePathToMintJson },
        builder
    });

    await builder.build({ outputDirectory: outputPath });

    await writeFile(
        join(
            AbsoluteFilePath.of(outputPath),
            RelativeFilePath.of(FERN_DIRECTORY),
            RelativeFilePath.of(PROJECT_CONFIG_FILENAME)
        ),
        JSON.stringify(
            {
                version: "*",
                organization: "fern"
            },
            undefined,
            4
        )
    );
}
