/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernOpenapiIr from "../../..";

/**
 * Note that for the oauth scheme we are currently assuming the resultant token is leveraged as a bearer token, e.g. "Authorization Bearer
 */
export interface OauthSecurityScheme {
    scopesEnum: FernOpenapiIr.EnumSchema | undefined;
    configuration: FernOpenapiIr.OAuthConfiguration | undefined;
}
