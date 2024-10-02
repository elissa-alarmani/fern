<?php

namespace Seed\Requests;

use Seed\Core\Json\SerializableType;
use Seed\Traits\ExampleType;
use Seed\Core\Json\JsonProperty;

class Inlined extends SerializableType
{
    use ExampleType;

    /**
     * @var string $unique
     */
    #[JsonProperty('unique')]
    public string $unique;

    /**
     * @param array{
     *   unique: string,
     *   name: string,
     *   docs: string,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->unique = $values['unique'];
        $this->name = $values['name'];
        $this->docs = $values['docs'];
    }
}
