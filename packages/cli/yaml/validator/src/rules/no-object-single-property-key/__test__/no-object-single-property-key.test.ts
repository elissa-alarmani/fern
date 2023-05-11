import { AbsoluteFilePath, join, RelativeFilePath } from "@fern-api/fs-utils";
import { getViolationsForRule } from "../../../testing-utils/getViolationsForRule";
import { ValidationViolation } from "../../../ValidationViolation";
import { NoObjectSinglePropertyKeyRule } from "../no-missing-union-variant-key";

describe("valid-field-names", () => {
    it("simple", async () => {
        const violations = await getViolationsForRule({
            rule: NoObjectSinglePropertyKeyRule,
            absolutePathToWorkspace: join(
                AbsoluteFilePath.of(__dirname),
                RelativeFilePath.of("fixtures"),
                RelativeFilePath.of("simple")
            ),
        });

        const expectedViolations: ValidationViolation[] = [
            {
                message: 'Union variant e has no type, so "key" cannot be defined',
                nodePath: ["types", "MyUnion"],
                relativeFilepath: RelativeFilePath.of("posts.yml"),
                severity: "error",
            },
        ];

        expect(violations).toEqual(expectedViolations);
    });
});
