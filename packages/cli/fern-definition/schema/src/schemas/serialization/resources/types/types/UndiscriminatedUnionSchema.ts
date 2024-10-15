/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { BaseTypeDeclarationSchema } from "./BaseTypeDeclarationSchema";
import { SingleUndiscriminatedUnionTypeSchema } from "./SingleUndiscriminatedUnionTypeSchema";

export const UndiscriminatedUnionSchema: core.serialization.ObjectSchema<
    serializers.UndiscriminatedUnionSchema.Raw,
    FernDefinition.UndiscriminatedUnionSchema
> = core.serialization
    .object({
        discriminated: core.serialization.booleanLiteral(false),
        extends: BaseTypeDeclarationSchema,
        union: core.serialization.list(SingleUndiscriminatedUnionTypeSchema).optional(),
    })
    .extend(BaseTypeDeclarationSchema);

export declare namespace UndiscriminatedUnionSchema {
    interface Raw extends BaseTypeDeclarationSchema.Raw {
        discriminated: false;
        extends: BaseTypeDeclarationSchema.Raw;
        union?: SingleUndiscriminatedUnionTypeSchema.Raw[] | null;
    }
}
