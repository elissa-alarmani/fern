//
//  Tree.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct Tree: Codable {

    enum CodingKeys: String, CodingKey {
        case nodes = "nodes"
    }

    public let nodes: [Node]?

    public init(nodes: [Node]? = nil) {
        self.nodes = nodes
    }

}
