//
//  NestedUser.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct NestedUser: Codable {

    enum CodingKeys: String, CodingKey {
        case name = "name"
        case user = "user"
    }

    public let name: String
    public let user: User

    public init(name: String, user: User) {
        self.name = name
        self.user = user
    }

}
