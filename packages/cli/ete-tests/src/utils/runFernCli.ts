import { loggingExeca } from "@fern-api/logging-execa";
import { ExecaChildProcess, Options } from "execa";
import path from "path";

export async function runFernCli(args: string[], options?: Options): Promise<ExecaChildProcess> {
    return loggingExeca(undefined, "node", [path.join(__dirname, "../../../cli/dist/dev/cli.cjs"), ...args], {
        ...options,
        env: {
            ...options?.env,
            FERN_TOKEN: "fern_WShoZn-n_QOXzXAsperx2FdZ7IUrqjYn"
        },
        doNotPipeOutput: options?.reject === false
    });
}
