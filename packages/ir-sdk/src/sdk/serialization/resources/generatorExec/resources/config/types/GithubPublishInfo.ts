/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as FernIr from "../../../../../../api/index";
import * as core from "../../../../../../core";
import { NpmGithubPublishInfo } from "./NpmGithubPublishInfo";
import { MavenGithubPublishInfo } from "./MavenGithubPublishInfo";
import { PostmanGithubPublishInfo } from "./PostmanGithubPublishInfo";
import { PypiGithubPublishInfo } from "./PypiGithubPublishInfo";
import { RubyGemsGithubPublishInfo } from "./RubyGemsGithubPublishInfo";
import { NugetGithubPublishInfo } from "./NugetGithubPublishInfo";

export const GithubPublishInfo: core.serialization.Schema<
    serializers.generatorExec.GithubPublishInfo.Raw,
    FernIr.generatorExec.GithubPublishInfo
> = core.serialization
    .union("type", {
        npm: NpmGithubPublishInfo,
        maven: MavenGithubPublishInfo,
        postman: PostmanGithubPublishInfo,
        pypi: PypiGithubPublishInfo,
        rubygems: RubyGemsGithubPublishInfo,
        nuget: NugetGithubPublishInfo,
    })
    .transform<FernIr.generatorExec.GithubPublishInfo>({
        transform: (value) => {
            switch (value.type) {
                case "npm":
                    return FernIr.generatorExec.GithubPublishInfo.npm(value);
                case "maven":
                    return FernIr.generatorExec.GithubPublishInfo.maven(value);
                case "postman":
                    return FernIr.generatorExec.GithubPublishInfo.postman(value);
                case "pypi":
                    return FernIr.generatorExec.GithubPublishInfo.pypi(value);
                case "rubygems":
                    return FernIr.generatorExec.GithubPublishInfo.rubygems(value);
                case "nuget":
                    return FernIr.generatorExec.GithubPublishInfo.nuget(value);
                default:
                    return value as FernIr.generatorExec.GithubPublishInfo;
            }
        },
        untransform: ({ _visit, ...value }) => value as any,
    });

export declare namespace GithubPublishInfo {
    type Raw =
        | GithubPublishInfo.Npm
        | GithubPublishInfo.Maven
        | GithubPublishInfo.Postman
        | GithubPublishInfo.Pypi
        | GithubPublishInfo.Rubygems
        | GithubPublishInfo.Nuget;

    interface Npm extends NpmGithubPublishInfo.Raw {
        type: "npm";
    }

    interface Maven extends MavenGithubPublishInfo.Raw {
        type: "maven";
    }

    interface Postman extends PostmanGithubPublishInfo.Raw {
        type: "postman";
    }

    interface Pypi extends PypiGithubPublishInfo.Raw {
        type: "pypi";
    }

    interface Rubygems extends RubyGemsGithubPublishInfo.Raw {
        type: "rubygems";
    }

    interface Nuget extends NugetGithubPublishInfo.Raw {
        type: "nuget";
    }
}
