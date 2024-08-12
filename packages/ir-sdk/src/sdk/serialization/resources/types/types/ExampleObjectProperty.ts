/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { NameAndWireValue } from "../../commons/types/NameAndWireValue";
import { DeclaredTypeName } from "./DeclaredTypeName";

export const ExampleObjectProperty: core.serialization.ObjectSchema<
    serializers.ExampleObjectProperty.Raw,
    FernIr.ExampleObjectProperty
> = core.serialization.objectWithoutOptionalProperties({
    name: NameAndWireValue,
    value: core.serialization.lazyObject(() => serializers.ExampleTypeReference),
    originalTypeDeclaration: DeclaredTypeName,
});

export declare namespace ExampleObjectProperty {
    interface Raw {
        name: NameAndWireValue.Raw;
        value: serializers.ExampleTypeReference.Raw;
        originalTypeDeclaration: DeclaredTypeName.Raw;
    }
}
