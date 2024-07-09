import { AstNode, Writer } from "@fern-api/generator-commons";
import Swift, { AccessLevel, Func, Import } from "../swift";

export declare namespace Class {
    interface Args {
        accessLevel?: AccessLevel;
        name: string;
        functions: Func[];
    }
}

export class Class extends AstNode {

    public readonly accessLevel?: AccessLevel;
    public readonly name: string;
    public readonly functions?: Func[];

    constructor({ 
        accessLevel, 
        name,
        functions
    }: Class.Args) {
        super(Swift.indentSize);
        this.accessLevel = accessLevel;
        this.name = name;
        this.functions = functions;
    }

    public write(writer: Writer): void {

        // e.g. public class ClassName {
        writer.openBlock([this.accessLevel, "class", this.name], "{", () => {

            writer.newLine();

            // TODO: Add fields

            // Add functions
            if (this.functions) {
                this.functions?.forEach(func => {
                    writer.writeNode(func);
                    writer.newLine();
                });
            }

        }, "}");

    }

}
