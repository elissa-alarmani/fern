import { AstNode, Writer } from "@fern-api/generator-commons";
import Swift, { AccessLevel, EnumCase, SwiftClass } from "..";

export declare namespace Enum {
    interface Args {
        accessLevel?: AccessLevel;
        name: string;
        inheritance?: SwiftClass[],
        enumCases: EnumCase[]
    }
}

export class Enum extends AstNode {

    public readonly accessLevel?: AccessLevel;
    public readonly name: string;
    public readonly inheritance?: SwiftClass[];
    public readonly enumCases: EnumCase[];

    constructor(args: Enum.Args) {
        super(Swift.indentSize);
        this.accessLevel = args.accessLevel;
        this.name = args.name;
        this.inheritance = args.inheritance;
        this.enumCases = args.enumCases;
    }

    private buildTitle(): string | undefined {

        if (!this.inheritance) {
            return this.name;
        }

        const names = this.inheritance.map(obj => obj.name).join(", ");
        return `${this.name}: ${names}`;

    }

    public write(writer: Writer): void {

        // example: public enum CodingKeys: String, CodingKey {
        writer.openBlock([this.accessLevel, "enum", this.buildTitle()], "{", () => {

            if (this.enumCases) {
                this.enumCases.forEach(value => {
                    writer.writeNode(value);
                });
            }

        }, "}");

    }

}
