/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";

export const InlineableTypeReferenceDeclarationWithNameSchema: core.serialization.Schema<
    serializers.InlineableTypeReferenceDeclarationWithNameSchema.Raw,
    FernDefinition.InlineableTypeReferenceDeclarationWithNameSchema
> = core.serialization.undiscriminatedUnion([
    core.serialization.string(),
    core.serialization.lazyObject(() => serializers.InlineableTypeReferenceDeclarationWithName),
]);

export declare namespace InlineableTypeReferenceDeclarationWithNameSchema {
    type Raw = string | serializers.InlineableTypeReferenceDeclarationWithName.Raw;
}
