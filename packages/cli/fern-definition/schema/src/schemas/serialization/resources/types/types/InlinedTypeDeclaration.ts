/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { InlinedEnumSchema } from "./InlinedEnumSchema";
import { InlinedDiscriminatedUnionSchema } from "./InlinedDiscriminatedUnionSchema";
import { InlinedUndiscriminatedUnionSchema } from "./InlinedUndiscriminatedUnionSchema";

export const InlinedTypeDeclaration: core.serialization.Schema<
    serializers.InlinedTypeDeclaration.Raw,
    FernDefinition.InlinedTypeDeclaration
> = core.serialization.undiscriminatedUnion([
    core.serialization.lazyObject(() => serializers.InlinedObjectSchema),
    InlinedEnumSchema,
    InlinedDiscriminatedUnionSchema,
    InlinedUndiscriminatedUnionSchema,
]);

export declare namespace InlinedTypeDeclaration {
    type Raw =
        | serializers.InlinedObjectSchema.Raw
        | InlinedEnumSchema.Raw
        | InlinedDiscriminatedUnionSchema.Raw
        | InlinedUndiscriminatedUnionSchema.Raw;
}
