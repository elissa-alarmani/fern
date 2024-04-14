/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernOpenapiIr from "../../..";

export interface ImplicitOAuthScheme extends FernOpenapiIr.BaseOauthSecurityScheme {
    authorizationCodeEnvVar: string | undefined;
    authorizationEndpoint: string;
    refreshEndpoint: string | undefined;
}
