import { ErrorDeclaration } from "@fern-fern/ir-model/errors";
import { IntermediateRepresentation } from "@fern-fern/ir-model/ir";
import { DeclaredTypeName, TypeDeclaration } from "@fern-fern/ir-model/types";
import { OpenAPIV3 } from "openapi-types";
import { convertServices } from "./converters/servicesConverter";
import { convertType } from "./converters/typeConverter";
import { constructEndpointSecurity, constructSecuritySchemes } from "./security";

export function convertToOpenApi({
    apiName,
    apiVersion,
    ir,
}: {
    apiName: string;
    apiVersion: string;
    ir: IntermediateRepresentation;
}): OpenAPIV3.Document | undefined {
    const schemas: Record<string, OpenAPIV3.ReferenceObject | OpenAPIV3.SchemaObject> = {};

    const typesByName: Record<string, TypeDeclaration> = {};
    ir.types.forEach((typeDeclaration) => {
        // convert type to open api schema
        const convertedType = convertType(typeDeclaration);
        schemas[convertedType.schemaName] = convertedType.openApiSchema;
        // populates typesByName map
        typesByName[getDeclaredTypeNameKey(typeDeclaration.name)] = typeDeclaration;
    });

    const errorsByName: Record<string, ErrorDeclaration> = {};
    ir.errors.forEach((errorDeclaration) => {
        errorsByName[getDeclaredTypeNameKey(errorDeclaration.name)] = errorDeclaration;
    });

    const security = constructEndpointSecurity(ir.auth);

    const paths = convertServices({
        httpServices: ir.services.http,
        typesByName,
        errorsByName,
        errorDiscriminationStrategy: ir.errorDiscriminationStrategy,
        security,
    });
    return {
        openapi: "3.0.1",
        info: {
            title: apiName,
            version: apiVersion,
        },
        paths,
        components: {
            schemas,
            securitySchemes: constructSecuritySchemes(ir.auth),
        },
        servers: ir.environments.map((environment) => {
            return {
                url: environment.url,
                docs: environment.docs,
            };
        }),
    };
}

export function getDeclaredTypeNameKey(declaredTypeName: DeclaredTypeName): string {
    return `${declaredTypeName.fernFilepath}-${declaredTypeName.name}`;
}
