/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../../../../index";

export interface NugetGithubPublishInfo {
    registryUrl: string;
    packageName: string;
    apiKeyEnvironmentVariable: FernIr.generatorExec.EnvironmentVariable;
    shouldGeneratePublishWorkflow: boolean | undefined;
}
