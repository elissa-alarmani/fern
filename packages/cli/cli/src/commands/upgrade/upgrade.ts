import { runMigrations } from "@fern-api/migrations";
import { getFernDirectory, loadProjectConfig } from "@fern-api/project-configuration";
import { loadProject } from "@fern-api/project-loader";
import { TASK_FAILURE } from "@fern-api/task-context";
import chalk from "chalk";
import { writeFile } from "fs/promises";
import produce from "immer";
import { CliContext } from "../../cli-context/CliContext";
import { isFernCliUpgradeAvailable } from "../../cli-context/upgrade-utils/isFernCliUpgradeAvailable";
import { rerunFernCliAtVersion } from "../../rerunFernCliAtVersion";
import { upgradeGeneratorsInWorkspaces } from "./upgradeGeneratorsInWorkspaces";

const PREVIOUS_VERSION_ENV_VAR = "FERN_PRE_UPGRADE_VERSION";

export async function upgrade({ cliContext }: { cliContext: CliContext }): Promise<void> {
    const fernCliUpgradeInfo = await isFernCliUpgradeAvailable(cliContext.environment);
    if (!fernCliUpgradeInfo.upgradeAvailable) {
        const previousVersion = process.env[PREVIOUS_VERSION_ENV_VAR];
        if (previousVersion == null) {
            cliContext.logger.info("No upgrade available.");
            return;
        } else {
            await cliContext.runTask(async (context) => {
                await runMigrations({
                    fromVersion: previousVersion,
                    toVersion: fernCliUpgradeInfo.latestVersion,
                    context,
                });
            });
            await cliContext.exitIfFailed();
        }

        const contextForLoadingProject = cliContext.addTask().start();
        const project = await loadProject({
            commandLineWorkspace: undefined,
            defaultToAllWorkspaces: true,
            cliName: cliContext.environment.cliName,
            context: contextForLoadingProject,
        });
        contextForLoadingProject.finish();
        if (project === TASK_FAILURE) {
            return cliContext.exit();
        }

        await upgradeGeneratorsInWorkspaces(project, cliContext);
    } else {
        const fernDirectory = await getFernDirectory();
        if (fernDirectory == null) {
            cliContext.fail("Could not find fern directory.");
            return cliContext.exit();
        }
        const projectConfig = await loadProjectConfig({ directory: fernDirectory });
        const newProjectConfig = produce(projectConfig.rawConfig, (draft) => {
            draft.version = fernCliUpgradeInfo.latestVersion;
        });
        await writeFile(projectConfig._absolutePath, JSON.stringify(newProjectConfig, undefined, 2));

        const message =
            "Upgraded {cliName} from" +
            chalk.dim(" {currentVersion}") +
            chalk.reset(" → ") +
            chalk.green("{latestVersion}");
        cliContext.logger.info(message);

        const { failed } = await rerunFernCliAtVersion({
            version: fernCliUpgradeInfo.latestVersion,
            cliEnvironment: cliContext.environment,
        });
        if (failed) {
            cliContext.fail();
        }
    }
}
