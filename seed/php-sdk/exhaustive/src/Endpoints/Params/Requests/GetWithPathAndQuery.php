<?php

namespace Seed\Endpoints\Params\Requests;

use Seed\Core\Json\SerializableType;

class GetWithPathAndQuery extends SerializableType
{
    /**
     * @var string $query
     */
    public string $query;

    /**
     * @param array{
     *   query: string,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->query = $values['query'];
    }
}
