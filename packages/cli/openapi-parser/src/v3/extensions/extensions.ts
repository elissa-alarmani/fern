import { Values } from "@fern-api/core-utils";

export const OpenAPIExtension = {
    /* This is an extension that several OpenAPI generators use that we support */
    ENUM_VAR_NAMES: "x-enum-varnames",
} as const;

export type OpenAPIExtension = Values<typeof OpenAPIExtension>;
