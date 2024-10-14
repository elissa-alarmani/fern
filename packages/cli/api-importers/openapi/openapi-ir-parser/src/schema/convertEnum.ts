import { Availability, EnumValue, SchemaWithExample, SdkGroupName, Source } from "@fern-api/openapi-ir";
import { camelCase, upperFirst } from "lodash-es";
import { FernEnumConfig } from "../openapi/v3/extensions/getFernEnum";
import { SchemaParserContext } from "./SchemaParserContext";
import { replaceStartingNumber } from "./utils/replaceStartingNumber";

export const VALID_ENUM_NAME_REGEX = /^[a-zA-Z][a-zA-Z0-9_]*$/;

export function convertEnum({
    nameOverride,
    generatedName,
    originalName,
    title,
    fernEnum,
    enumVarNames,
    enumValues,
    _default,
    description,
    availability,
    wrapAsNullable,
    groupName,
    context,
    source
}: {
    nameOverride: string | undefined;
    generatedName: string;
    originalName: string | undefined;
    title: string | undefined;
    fernEnum: FernEnumConfig | undefined;
    enumVarNames: string[] | undefined;
    enumValues: string[];
    _default: string | undefined;
    description: string | undefined;
    availability: Availability | undefined;
    wrapAsNullable: boolean;
    groupName: SdkGroupName | undefined;
    context: SchemaParserContext | undefined;
    source: Source;
}): SchemaWithExample {
    const strippedEnumVarNames = stripCommonPrefix(enumVarNames ?? []);
    const uniqueValues = new Set(enumValues);
    const values = Array.from(uniqueValues).map((value, index): EnumValue => {
        const fernEnumValue = fernEnum?.[value];
        const enumVarName = strippedEnumVarNames[index];
        const valueIsValidName = VALID_ENUM_NAME_REGEX.test(value);
        let nameOverride = fernEnumValue?.name ?? enumVarName;
        const generatedName = valueIsValidName ? value : generateEnumNameFromValue(value);

        if (nameOverride != null && !VALID_ENUM_NAME_REGEX.test(nameOverride)) {
            context?.logger.warn(
                `Enum name override ${nameOverride} is not a valid name. Falling back on ${generatedName}.`
            );
            nameOverride = undefined;
        }

        return {
            nameOverride,
            generatedName,
            value,
            description: fernEnumValue?.description,
            availability,
            casing: {
                snake: fernEnumValue?.casing?.snake ?? undefined,
                pascal: fernEnumValue?.casing?.pascal ?? undefined,
                screamingSnake: fernEnumValue?.casing?.screamingSnake ?? undefined,
                camel: fernEnumValue?.casing?.camel ?? undefined
            }
        };
    });
    const _defaultEnumValue = _default != null ? values.find((value) => value.value === _default) : undefined;
    return wrapEnum({
        wrapAsNullable,
        nameOverride,
        generatedName,
        originalName,
        title,
        values,
        _default: _defaultEnumValue,
        description,
        availability,
        groupName,
        source
    });
}

export function wrapEnum({
    wrapAsNullable,
    nameOverride,
    generatedName,
    originalName,
    title,
    values,
    _default,
    description,
    availability,
    groupName,
    source
}: {
    wrapAsNullable: boolean;
    nameOverride: string | undefined;
    generatedName: string;
    originalName: string | undefined;
    title: string | undefined;
    values: EnumValue[];
    _default: EnumValue | undefined;
    description: string | undefined;
    availability: Availability | undefined;
    groupName: SdkGroupName | undefined;
    source: Source;
}): SchemaWithExample {
    if (wrapAsNullable) {
        return SchemaWithExample.nullable({
            nameOverride,
            generatedName,
            originalName,
            title,
            value: SchemaWithExample.enum({
                nameOverride,
                generatedName,
                originalName,
                title,
                values,
                description,
                default: _default,
                availability,
                example: undefined,
                groupName,
                source
            }),
            description,
            availability,
            groupName
        });
    }
    return SchemaWithExample.enum({
        nameOverride,
        generatedName,
        originalName,
        title,
        values,
        description,
        availability,
        default: _default,
        example: undefined,
        groupName,
        source
    });
}

const HARDCODED_ENUM_NAMES: Record<string, string> = {
    "<": "LESS_THAN",
    ">": "GREATER_THAN",
    ">=": "GREATER_THAN_OR_EQUAL_TO",
    "<=": "LESS_THAN_OR_EQUAL_TO",
    "!=": "NOT_EQUALS",
    "=": "EQUAL_TO",
    "==": "EQUAL_TO",
    "*": "ALL",
    "": "EMPTY",
    '""': "EMPTY_STRING",
    "-": "HYPHEN",
    "|": "PIPE",
    ".": "DOT",
    "/": "SLASH"
};

export function generateEnumNameFromValue(value: string): string {
    const maybeParsedNumber = replaceStartingNumber(value);
    const maybeHardcodedEnumName = HARDCODED_ENUM_NAMES[value];
    if (maybeParsedNumber != null) {
        return upperFirst(camelCase(maybeParsedNumber));
    } else if (maybeHardcodedEnumName != null) {
        return maybeHardcodedEnumName;
    } else {
        if (value.toLowerCase() === "n/a") {
            return "NOT_APPLICABLE";
        }
        return upperFirst(camelCase(value));
    }
}

function stripCommonPrefix(names: string[]): string[] {
    if (names.length <= 1 || names[0] == null) {
        return names;
    }

    const nameZero = names[0];

    let i = 0;
    // while all words have the same character at position i, increment i
    while (nameZero[i] != null && names.every((name) => name[i] === nameZero[i])) {
        i++;
    }

    // prefix is the substring from the beginning to the last successfully checked i
    return names.map((name) => name.substring(i));
}
