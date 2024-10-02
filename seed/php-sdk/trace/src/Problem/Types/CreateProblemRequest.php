<?php

namespace Seed\Problem\Types;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;
use Seed\Commons\Types\Language;
use Seed\Core\Types\ArrayType;
use Seed\Commons\Types\TestCaseWithExpectedResult;

class CreateProblemRequest extends SerializableType
{
    /**
     * @var string $problemName
     */
    #[JsonProperty('problemName')]
    public string $problemName;

    /**
     * @var ProblemDescription $problemDescription
     */
    #[JsonProperty('problemDescription')]
    public ProblemDescription $problemDescription;

    /**
     * @var array<value-of<Language>, ProblemFiles> $files
     */
    #[JsonProperty('files'), ArrayType(['string' => ProblemFiles::class])]
    public array $files;

    /**
     * @var array<VariableTypeAndName> $inputParams
     */
    #[JsonProperty('inputParams'), ArrayType([VariableTypeAndName::class])]
    public array $inputParams;

    /**
     * @var mixed $outputType
     */
    #[JsonProperty('outputType')]
    public mixed $outputType;

    /**
     * @var array<TestCaseWithExpectedResult> $testcases
     */
    #[JsonProperty('testcases'), ArrayType([TestCaseWithExpectedResult::class])]
    public array $testcases;

    /**
     * @var string $methodName
     */
    #[JsonProperty('methodName')]
    public string $methodName;

    /**
     * @param array{
     *   problemName: string,
     *   problemDescription: ProblemDescription,
     *   files: array<value-of<Language>, ProblemFiles>,
     *   inputParams: array<VariableTypeAndName>,
     *   outputType: mixed,
     *   testcases: array<TestCaseWithExpectedResult>,
     *   methodName: string,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->problemName = $values['problemName'];
        $this->problemDescription = $values['problemDescription'];
        $this->files = $values['files'];
        $this->inputParams = $values['inputParams'];
        $this->outputType = $values['outputType'];
        $this->testcases = $values['testcases'];
        $this->methodName = $values['methodName'];
    }
}
