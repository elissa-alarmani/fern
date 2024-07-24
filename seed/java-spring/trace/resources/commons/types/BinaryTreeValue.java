/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.commons.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(
    builder = BinaryTreeValue.Builder.class
)
public final class BinaryTreeValue {
  private final Optional<NodeId> root;

  private final Map<NodeId, BinaryTreeNodeValue> nodes;

  private BinaryTreeValue(Optional<NodeId> root, Map<NodeId, BinaryTreeNodeValue> nodes) {
    this.root = root;
    this.nodes = nodes;
  }

  @JsonProperty("root")
  public Optional<NodeId> getRoot() {
    return root;
  }

  @JsonProperty("nodes")
  public Map<NodeId, BinaryTreeNodeValue> getNodes() {
    return nodes;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof BinaryTreeValue && equalTo((BinaryTreeValue) other);
  }

  private boolean equalTo(BinaryTreeValue other) {
    return root.equals(other.root) && nodes.equals(other.nodes);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.root, this.nodes);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static Builder builder() {
    return new Builder();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder {
    private Optional<NodeId> root = Optional.empty();

    private Map<NodeId, BinaryTreeNodeValue> nodes = new LinkedHashMap<>();

    private Builder() {
    }

    public Builder from(BinaryTreeValue other) {
      root(other.getRoot());
      nodes(other.getNodes());
      return this;
    }

    @JsonSetter(
        value = "root",
        nulls = Nulls.SKIP
    )
    public Builder root(Optional<NodeId> root) {
      this.root = root;
      return this;
    }

    public Builder root(NodeId root) {
      this.root = Optional.ofNullable(root);
      return this;
    }

    @JsonSetter(
        value = "nodes",
        nulls = Nulls.SKIP
    )
    public Builder nodes(Map<NodeId, BinaryTreeNodeValue> nodes) {
      this.nodes.clear();
      this.nodes.putAll(nodes);
      return this;
    }

    public Builder putAllNodes(Map<NodeId, BinaryTreeNodeValue> nodes) {
      this.nodes.putAll(nodes);
      return this;
    }

    public Builder nodes(NodeId key, BinaryTreeNodeValue value) {
      this.nodes.put(key, value);
      return this;
    }

    public BinaryTreeValue build() {
      return new BinaryTreeValue(root, nodes);
    }
  }
}
