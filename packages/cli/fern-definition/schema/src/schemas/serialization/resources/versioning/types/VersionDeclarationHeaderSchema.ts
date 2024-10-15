/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { VersionDeclarationHeaderObjectSchema } from "./VersionDeclarationHeaderObjectSchema";

export const VersionDeclarationHeaderSchema: core.serialization.Schema<
    serializers.VersionDeclarationHeaderSchema.Raw,
    FernDefinition.VersionDeclarationHeaderSchema
> = core.serialization.undiscriminatedUnion([core.serialization.string(), VersionDeclarationHeaderObjectSchema]);

export declare namespace VersionDeclarationHeaderSchema {
    type Raw = string | VersionDeclarationHeaderObjectSchema.Raw;
}
