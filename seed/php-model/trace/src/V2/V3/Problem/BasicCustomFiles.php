<?php

namespace Seed\V2\V3\Problem;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;
use Seed\Commons\Language;
use Seed\Core\Types\ArrayType;

class BasicCustomFiles extends SerializableType
{
    /**
     * @var string $methodName
     */
    #[JsonProperty('methodName')]
    public string $methodName;

    /**
     * @var NonVoidFunctionSignature $signature
     */
    #[JsonProperty('signature')]
    public NonVoidFunctionSignature $signature;

    /**
     * @var array<value-of<Language>, Files> $additionalFiles
     */
    #[JsonProperty('additionalFiles'), ArrayType(['string' => Files::class])]
    public array $additionalFiles;

    /**
     * @var BasicTestCaseTemplate $basicTestCaseTemplate
     */
    #[JsonProperty('basicTestCaseTemplate')]
    public BasicTestCaseTemplate $basicTestCaseTemplate;

    /**
     * @param array{
     *   methodName: string,
     *   signature: NonVoidFunctionSignature,
     *   additionalFiles: array<value-of<Language>, Files>,
     *   basicTestCaseTemplate: BasicTestCaseTemplate,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->methodName = $values['methodName'];
        $this->signature = $values['signature'];
        $this->additionalFiles = $values['additionalFiles'];
        $this->basicTestCaseTemplate = $values['basicTestCaseTemplate'];
    }
}
