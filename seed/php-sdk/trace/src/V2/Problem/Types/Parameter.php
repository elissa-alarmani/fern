<?php

namespace Seed\V2\Problem\Types;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class Parameter extends SerializableType
{
    /**
     * @var string $parameterId
     */
    #[JsonProperty('parameterId')]
    public string $parameterId;

    /**
     * @var string $name
     */
    #[JsonProperty('name')]
    public string $name;

    /**
     * @var mixed $variableType
     */
    #[JsonProperty('variableType')]
    public mixed $variableType;

    /**
     * @param array{
     *   parameterId: string,
     *   name: string,
     *   variableType: mixed,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->parameterId = $values['parameterId'];
        $this->name = $values['name'];
        $this->variableType = $values['variableType'];
    }
}
