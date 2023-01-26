import { DeclaredServiceName } from "@fern-fern/ir-model/http";
import { ExportedFilePath, Reference } from "@fern-typescript/commons";
import { AbstractExpressServiceDeclarationReferencer } from "./AbstractExpressServiceDeclarationReferencer";
import { DeclarationReferencer } from "./DeclarationReferencer";

export class ExpressServiceDeclarationReferencer extends AbstractExpressServiceDeclarationReferencer<DeclaredServiceName> {
    public getExportedFilepath(name: DeclaredServiceName): ExportedFilePath {
        return {
            directories: [...this.getExportedDirectory(name.fernFilepath)],
            file: {
                nameOnDisk: this.getFilename(name),
                exportDeclaration: {
                    namedExports: [this.getExportedName(name)],
                },
            },
        };
    }

    public getFilename(name: DeclaredServiceName): string {
        return `${this.getExportedName(name)}.ts`;
    }

    public getExportedName(name: DeclaredServiceName): string {
        return `Abstract${name.name.pascalCase.unsafeName}`;
    }

    public getReferenceToService(args: DeclarationReferencer.getReferenceTo.Options<DeclaredServiceName>): Reference {
        return this.getReferenceTo(this.getExportedName(args.name), args);
    }
}
