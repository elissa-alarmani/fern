<?php

namespace Seed\Commons\Types;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class KeyValuePair extends SerializableType
{
    /**
     * @var mixed $key
     */
    #[JsonProperty('key')]
    public mixed $key;

    /**
     * @var mixed $value
     */
    #[JsonProperty('value')]
    public mixed $value;

    /**
     * @param array{
     *   key: mixed,
     *   value: mixed,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->key = $values['key'];
        $this->value = $values['value'];
    }
}
