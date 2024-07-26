//
//  User.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct User: Codable {

    enum CodingKeys: String, CodingKey {
        case id = "id"
        case name = "name"
        case age = "age"
    }

    public let id: String

    /// The user's name. This name is unique to each user. A few examples are included below:
    /// 
    /// - Alice
    /// - Bob
    /// - Charlie
    public let name: String

    /// The user's age.
    public let age: Int?

    /// A user object. This type is used throughout the following APIs:
    /// 
    /// - createUser
    /// - getUser
    public init(id: String, name: String, age: Int? = nil) {
        self.id = id
        self.name = name
        self.age = age
    }

}
