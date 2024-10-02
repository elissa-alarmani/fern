<?php

namespace Seed;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class Parent_ extends SerializableType
{
    /**
     * @var string $parent
     */
    #[JsonProperty('parent')]
    public string $parent;

    /**
     * @param array{
     *   parent: string,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->parent = $values['parent'];
    }
}
