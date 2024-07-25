//
//  Node.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct Node: Codable {

    enum CodingKeys: String, CodingKey {
        case id = "id"
        case label = "label"
        case metadata = "metadata"
    }

    public let id: String
    public let label: String?
    public let metadata: Metadata?

}
