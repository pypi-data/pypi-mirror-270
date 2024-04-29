from dataclasses import dataclass
from typing import Optional, Any, Union, Literal, List


@dataclass
class KayocError:
    succes: bool
    message: str
    done: bool
    error: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "KayocError":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
            error=data["error"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["error"] = self.error

        return data

    @classmethod
    def example(cls) -> "KayocError":
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
            error="The only thing your eyes haven't told me is your name 👀🤔",
        )


@dataclass
class CreateDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateDatabaseRequest":
        return cls(
            database_name=data["database_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> "CreateDatabaseRequest":
        return cls(
            database_name="Just like a fine wine, you get better with age 🍷👵",
        )


@dataclass
class DatabasePermission:
    user_id: int
    user_name: str
    database_id: int
    type: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabasePermission":
        return cls(
            user_id=data["user_id"],
            user_name=data["user_name"],
            database_id=data["database_id"],
            type=data["type"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["user_id"] = self.user_id
        data["user_name"] = self.user_name
        data["database_id"] = self.database_id
        data["type"] = self.type

        return data

    @classmethod
    def example(cls) -> "DatabasePermission":
        return cls(
            user_id=666,
            user_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            database_id=666,
            type="Hi, its kayoc here 😉💅",
        )


@dataclass
class CreateDatabaseResponse:
    database_id: int
    permissions: list[DatabasePermission]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateDatabaseResponse":
        return cls(
            database_id=data["database_id"],
            permissions=[
                DatabasePermission.from_json(item) for item in data["permissions"]
            ],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["permissions"] = [
            DatabasePermission.to_json(item) for item in self.permissions
        ]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateDatabaseResponse":
        return cls(
            database_id=666,
            permissions=[
                DatabasePermission.example(),
                DatabasePermission.example(),
                DatabasePermission.example(),
                DatabasePermission.example(),
                DatabasePermission.example(),
                DatabasePermission.example(),
                DatabasePermission.example(),
            ],
            succes=True,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=False,
        )


@dataclass
class DeleteDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteDatabaseRequest":
        return cls(
            database_name=data["database_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> "DeleteDatabaseRequest":
        return cls(
            database_name="Hi, its kayoc here 😉💅",
        )


@dataclass
class DeleteDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteDatabaseResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DeleteDatabaseResponse":
        return cls(
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )


@dataclass
class DatabaseInfoRequest:
    database_name: Optional[str]
    database_id: Optional[int]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseInfoRequest":
        return cls(
            database_name=data["database_name"] if "database_name" in data else None,
            database_id=data["database_id"] if "database_id" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.database_name is not None:
            data["database_name"] = self.database_name

        if self.database_id is not None:
            data["database_id"] = self.database_id

        return data

    @classmethod
    def example(cls) -> "DatabaseInfoRequest":
        return cls(
            database_name=None,
            database_id=None,
        )


@dataclass
class UserDatabasePermissionInfo:
    user_id: int
    user_name: str
    type: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UserDatabasePermissionInfo":
        return cls(
            user_id=data["user_id"],
            user_name=data["user_name"],
            type=data["type"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["user_id"] = self.user_id
        data["user_name"] = self.user_name
        data["type"] = self.type

        return data

    @classmethod
    def example(cls) -> "UserDatabasePermissionInfo":
        return cls(
            user_id=69,
            user_name="I'm not a photographer, but I can picture us together 📸👫",
            type="I'm not a photographer, but I can picture us together 📸👫",
        )


@dataclass
class DataBaseInfoSubFolder:
    folder_id: int
    name: str
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DataBaseInfoSubFolder":
        return cls(
            folder_id=data["folder_id"],
            name=data["name"],
            description=data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name

        if self.description is not None:
            data["description"] = self.description

        return data

    @classmethod
    def example(cls) -> "DataBaseInfoSubFolder":
        return cls(
            folder_id=666,
            name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            description=None,
        )


@dataclass
class DatabaseInfoItem:
    item_id: int
    name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseInfoItem":
        return cls(
            item_id=data["item_id"],
            name=data["name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["item_id"] = self.item_id
        data["name"] = self.name

        return data

    @classmethod
    def example(cls) -> "DatabaseInfoItem":
        return cls(
            item_id=420,
            name="I'm not a photographer, but I can picture us together 📸👫",
        )


@dataclass
class DatabaseInfoFolder:
    folder_id: int
    name: str
    subfolders: list[DataBaseInfoSubFolder]
    items: list[DatabaseInfoItem]
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseInfoFolder":
        return cls(
            folder_id=data["folder_id"],
            name=data["name"],
            subfolders=[
                DataBaseInfoSubFolder.from_json(item) for item in data["subfolders"]
            ],
            items=[DatabaseInfoItem.from_json(item) for item in data["items"]],
            description=data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name
        data["subfolders"] = [
            DataBaseInfoSubFolder.to_json(item) for item in self.subfolders
        ]
        data["items"] = [DatabaseInfoItem.to_json(item) for item in self.items]

        if self.description is not None:
            data["description"] = self.description

        return data

    @classmethod
    def example(cls) -> "DatabaseInfoFolder":
        return cls(
            folder_id=666,
            name="Wanna go out? No strings attached 🍆🍑",
            subfolders=[
                DataBaseInfoSubFolder.example(),
                DataBaseInfoSubFolder.example(),
                DataBaseInfoSubFolder.example(),
                DataBaseInfoSubFolder.example(),
                DataBaseInfoSubFolder.example(),
                DataBaseInfoSubFolder.example(),
            ],
            items=[DatabaseInfoItem.example()],
            description=None,
        )


@dataclass
class DateTime:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DateTime":
        return cls(
            year=data["year"],
            month=data["month"],
            day=data["day"],
            hour=data["hour"],
            minute=data["minute"],
            second=data["second"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["year"] = self.year
        data["month"] = self.month
        data["day"] = self.day
        data["hour"] = self.hour
        data["minute"] = self.minute
        data["second"] = self.second

        return data

    @classmethod
    def example(cls) -> "DateTime":
        return cls(
            year=666,
            month=666,
            day=420,
            hour=666,
            minute=69,
            second=420,
        )


@dataclass
class DatabaseInfoBuild:
    build_id: int
    name: str
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseInfoBuild":
        return cls(
            build_id=data["build_id"],
            name=data["name"],
            created_at=DateTime.from_json(data["created_at"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id
        data["name"] = self.name
        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> "DatabaseInfoBuild":
        return cls(
            build_id=69,
            name="The only thing your eyes haven't told me is your name 👀🤔",
            created_at=DateTime.example(),
        )


@dataclass
class DatabaseInfoResponse:
    database_id: int
    name: str
    description: Optional[str]
    is_public: bool
    permissions: list[UserDatabasePermissionInfo]
    folder: DatabaseInfoFolder
    builds: list[DatabaseInfoBuild]
    created_at: DateTime
    size_bytes: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseInfoResponse":
        return cls(
            database_id=data["database_id"],
            name=data["name"],
            description=data["description"] if "description" in data else None,
            is_public=data["is_public"],
            permissions=[
                UserDatabasePermissionInfo.from_json(item)
                for item in data["permissions"]
            ],
            folder=DatabaseInfoFolder.from_json(data["folder"]),
            builds=[DatabaseInfoBuild.from_json(item) for item in data["builds"]],
            created_at=DateTime.from_json(data["created_at"]),
            size_bytes=data["size_bytes"],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name

        if self.description is not None:
            data["description"] = self.description

        data["is_public"] = self.is_public
        data["permissions"] = [
            UserDatabasePermissionInfo.to_json(item) for item in self.permissions
        ]
        data["folder"] = self.folder.to_json()
        data["builds"] = [DatabaseInfoBuild.to_json(item) for item in self.builds]
        data["created_at"] = self.created_at.to_json()
        data["size_bytes"] = self.size_bytes
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DatabaseInfoResponse":
        return cls(
            database_id=666,
            name="Hi, its kayoc here 😉💅",
            description="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            is_public=True,
            permissions=[
                UserDatabasePermissionInfo.example(),
                UserDatabasePermissionInfo.example(),
                UserDatabasePermissionInfo.example(),
                UserDatabasePermissionInfo.example(),
            ],
            folder=DatabaseInfoFolder.example(),
            builds=[
                DatabaseInfoBuild.example(),
                DatabaseInfoBuild.example(),
                DatabaseInfoBuild.example(),
                DatabaseInfoBuild.example(),
                DatabaseInfoBuild.example(),
                DatabaseInfoBuild.example(),
                DatabaseInfoBuild.example(),
            ],
            created_at=DateTime.example(),
            size_bytes=69,
            succes=True,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=True,
        )


@dataclass
class RenameDatabaseRequest:
    database_name: str
    new_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameDatabaseRequest":
        return cls(
            database_name=data["database_name"],
            new_name=data["new_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> "RenameDatabaseRequest":
        return cls(
            database_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            new_name="I'm not a photographer, but I can picture us together 📸👫",
        )


@dataclass
class RenameDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameDatabaseResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RenameDatabaseResponse":
        return cls(
            succes=False,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=True,
        )


@dataclass
class DatabaseUpdateDescriptionRequest:
    database_name: str
    new_description: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseUpdateDescriptionRequest":
        return cls(
            database_name=data["database_name"],
            new_description=data["new_description"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name
        data["new_description"] = self.new_description

        return data

    @classmethod
    def example(cls) -> "DatabaseUpdateDescriptionRequest":
        return cls(
            database_name="Wanna go out? No strings attached 🍆🍑",
            new_description="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
        )


@dataclass
class DatabaseUpdateDescriptionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseUpdateDescriptionResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DatabaseUpdateDescriptionResponse":
        return cls(
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )


@dataclass
class DatabaseBrowseRequest:
    fuzzy_database_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseBrowseRequest":
        return cls(
            fuzzy_database_name=data["fuzzy_database_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["fuzzy_database_name"] = self.fuzzy_database_name

        return data

    @classmethod
    def example(cls) -> "DatabaseBrowseRequest":
        return cls(
            fuzzy_database_name="Wanna go out? No strings attached 🍆🍑",
        )


@dataclass
class BrowseDatabaseInfo:
    database_id: int
    name: str
    owner_email: Optional[str]
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BrowseDatabaseInfo":
        return cls(
            database_id=data["database_id"],
            name=data["name"],
            owner_email=data["owner_email"] if "owner_email" in data else None,
            description=data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name

        if self.owner_email is not None:
            data["owner_email"] = self.owner_email

        if self.description is not None:
            data["description"] = self.description

        return data

    @classmethod
    def example(cls) -> "BrowseDatabaseInfo":
        return cls(
            database_id=69,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            owner_email="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            description=None,
        )


@dataclass
class DatabaseBrowseResponse:
    databases: list[BrowseDatabaseInfo]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseBrowseResponse":
        return cls(
            databases=[
                BrowseDatabaseInfo.from_json(item) for item in data["databases"]
            ],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["databases"] = [
            BrowseDatabaseInfo.to_json(item) for item in self.databases
        ]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DatabaseBrowseResponse":
        return cls(
            databases=[
                BrowseDatabaseInfo.example(),
                BrowseDatabaseInfo.example(),
                BrowseDatabaseInfo.example(),
                BrowseDatabaseInfo.example(),
            ],
            succes=False,
            message="You've got character! ㍼🥴",
            done=True,
        )


@dataclass
class DatabaseUpdatePermissionRequest:
    database_name: str
    user_email: str
    new_permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseUpdatePermissionRequest":
        return cls(
            database_name=data["database_name"],
            user_email=data["user_email"],
            new_permission=data["new_permission"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name
        data["user_email"] = self.user_email
        data["new_permission"] = self.new_permission

        return data

    @classmethod
    def example(cls) -> "DatabaseUpdatePermissionRequest":
        return cls(
            database_name="You've got character! ㍼🥴",
            user_email="You've got character! ㍼🥴",
            new_permission="read",
        )


@dataclass
class DatabaseUpdatePermissionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseUpdatePermissionResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DatabaseUpdatePermissionResponse":
        return cls(
            succes=False,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )


@dataclass
class PublishDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "PublishDatabaseRequest":
        return cls(
            database_name=data["database_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> "PublishDatabaseRequest":
        return cls(
            database_name="Hi, its kayoc here 😉💅",
        )


@dataclass
class PublishDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "PublishDatabaseResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "PublishDatabaseResponse":
        return cls(
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )


@dataclass
class UnpublishDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UnpublishDatabaseRequest":
        return cls(
            database_name=data["database_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> "UnpublishDatabaseRequest":
        return cls(
            database_name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
        )


@dataclass
class UnpublishDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UnpublishDatabaseResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UnpublishDatabaseResponse":
        return cls(
            succes=False,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=True,
        )


@dataclass
class DatabaseListDatabase:
    database_id: int
    name: str
    description: Optional[str]
    is_public: bool
    created_at: DateTime
    size_bytes: int
    nitems: int
    nbuilds: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseListDatabase":
        return cls(
            database_id=data["database_id"],
            name=data["name"],
            description=data["description"] if "description" in data else None,
            is_public=data["is_public"],
            created_at=DateTime.from_json(data["created_at"]),
            size_bytes=data["size_bytes"],
            nitems=data["nitems"],
            nbuilds=data["nbuilds"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name

        if self.description is not None:
            data["description"] = self.description

        data["is_public"] = self.is_public
        data["created_at"] = self.created_at.to_json()
        data["size_bytes"] = self.size_bytes
        data["nitems"] = self.nitems
        data["nbuilds"] = self.nbuilds

        return data

    @classmethod
    def example(cls) -> "DatabaseListDatabase":
        return cls(
            database_id=666,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            description="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            is_public=True,
            created_at=DateTime.example(),
            size_bytes=666,
            nitems=69,
            nbuilds=666,
        )


@dataclass
class DatabaseListResponse:
    databases: list[DatabaseListDatabase]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseListResponse":
        return cls(
            databases=[
                DatabaseListDatabase.from_json(item) for item in data["databases"]
            ],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["databases"] = [
            DatabaseListDatabase.to_json(item) for item in self.databases
        ]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DatabaseListResponse":
        return cls(
            databases=[
                DatabaseListDatabase.example(),
                DatabaseListDatabase.example(),
                DatabaseListDatabase.example(),
                DatabaseListDatabase.example(),
                DatabaseListDatabase.example(),
            ],
            succes=False,
            message="You've got character! ㍼🥴",
            done=False,
        )


@dataclass
class QuestionInfoRequest:
    question_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionInfoRequest":
        return cls(
            question_id=data["question_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["question_id"] = self.question_id

        return data

    @classmethod
    def example(cls) -> "QuestionInfoRequest":
        return cls(
            question_id=69,
        )


@dataclass
class QuestionInfoAnswerRating:
    rating: Literal["down", "neutral", "up"]
    user_id: int
    user_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionInfoAnswerRating":
        return cls(
            rating=data["rating"],
            user_id=data["user_id"],
            user_name=data["user_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["rating"] = self.rating
        data["user_id"] = self.user_id
        data["user_name"] = self.user_name

        return data

    @classmethod
    def example(cls) -> "QuestionInfoAnswerRating":
        return cls(
            rating="neutral",
            user_id=69,
            user_name="Just like a fine wine, you get better with age 🍷👵",
        )


@dataclass
class QuestionInfoAnswer:
    content: str
    explanation: str
    ratings: list[QuestionInfoAnswerRating]
    answer_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionInfoAnswer":
        return cls(
            content=data["content"],
            explanation=data["explanation"],
            ratings=[
                QuestionInfoAnswerRating.from_json(item) for item in data["ratings"]
            ],
            answer_id=data["answer_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["content"] = self.content
        data["explanation"] = self.explanation
        data["ratings"] = [
            QuestionInfoAnswerRating.to_json(item) for item in self.ratings
        ]
        data["answer_id"] = self.answer_id

        return data

    @classmethod
    def example(cls) -> "QuestionInfoAnswer":
        return cls(
            content="Hi, its kayoc here 😉💅",
            explanation="You've got character! ㍼🥴",
            ratings=[
                QuestionInfoAnswerRating.example(),
                QuestionInfoAnswerRating.example(),
                QuestionInfoAnswerRating.example(),
            ],
            answer_id=69,
        )


@dataclass
class QuestionInfoMessage:
    answer: QuestionInfoAnswer
    content: str
    created_at: DateTime
    message_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionInfoMessage":
        return cls(
            answer=QuestionInfoAnswer.from_json(data["answer"]),
            content=data["content"],
            created_at=DateTime.from_json(data["created_at"]),
            message_id=data["message_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["answer"] = self.answer.to_json()
        data["content"] = self.content
        data["created_at"] = self.created_at.to_json()
        data["message_id"] = self.message_id

        return data

    @classmethod
    def example(cls) -> "QuestionInfoMessage":
        return cls(
            answer=QuestionInfoAnswer.example(),
            content="The only thing your eyes haven't told me is your name 👀🤔",
            created_at=DateTime.example(),
            message_id=420,
        )


@dataclass
class QuestionInfoResponse:
    question_id: int
    name: Optional[str]
    created_at: DateTime
    messages: list[QuestionInfoMessage]
    build_name: str
    build_id: int
    user_id: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionInfoResponse":
        return cls(
            question_id=data["question_id"],
            name=data["name"] if "name" in data else None,
            created_at=DateTime.from_json(data["created_at"]),
            messages=[QuestionInfoMessage.from_json(item) for item in data["messages"]],
            build_name=data["build_name"],
            build_id=data["build_id"],
            user_id=data["user_id"],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["question_id"] = self.question_id

        if self.name is not None:
            data["name"] = self.name

        data["created_at"] = self.created_at.to_json()
        data["messages"] = [QuestionInfoMessage.to_json(item) for item in self.messages]
        data["build_name"] = self.build_name
        data["build_id"] = self.build_id
        data["user_id"] = self.user_id
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "QuestionInfoResponse":
        return cls(
            question_id=666,
            name=None,
            created_at=DateTime.example(),
            messages=[
                QuestionInfoMessage.example(),
                QuestionInfoMessage.example(),
                QuestionInfoMessage.example(),
                QuestionInfoMessage.example(),
                QuestionInfoMessage.example(),
            ],
            build_name="Just like a fine wine, you get better with age 🍷👵",
            build_id=420,
            user_id=666,
            succes=False,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=False,
        )


@dataclass
class QuestionListQuestion:
    name: str
    question_id: int
    created_at: DateTime
    nmessages: int
    build_name: str
    build_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionListQuestion":
        return cls(
            name=data["name"],
            question_id=data["question_id"],
            created_at=DateTime.from_json(data["created_at"]),
            nmessages=data["nmessages"],
            build_name=data["build_name"],
            build_id=data["build_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["name"] = self.name
        data["question_id"] = self.question_id
        data["created_at"] = self.created_at.to_json()
        data["nmessages"] = self.nmessages
        data["build_name"] = self.build_name
        data["build_id"] = self.build_id

        return data

    @classmethod
    def example(cls) -> "QuestionListQuestion":
        return cls(
            name="Just like a fine wine, you get better with age 🍷👵",
            question_id=69,
            created_at=DateTime.example(),
            nmessages=420,
            build_name="I'm not a photographer, but I can picture us together 📸👫",
            build_id=666,
        )


@dataclass
class QuestionListResponse:
    questions: list[QuestionListQuestion]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "QuestionListResponse":
        return cls(
            questions=[
                QuestionListQuestion.from_json(item) for item in data["questions"]
            ],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["questions"] = [
            QuestionListQuestion.to_json(item) for item in self.questions
        ]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "QuestionListResponse":
        return cls(
            questions=[QuestionListQuestion.example(), QuestionListQuestion.example()],
            succes=False,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=False,
        )


@dataclass
class UpdateQuestionNameRequest:
    question_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateQuestionNameRequest":
        return cls(
            question_id=data["question_id"],
            new_name=data["new_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["question_id"] = self.question_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> "UpdateQuestionNameRequest":
        return cls(
            question_id=420,
            new_name="I'm not a photographer, but I can picture us together 📸👫",
        )


@dataclass
class UpdateQuestionNameResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateQuestionNameResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateQuestionNameResponse":
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )


@dataclass
class AnswerConfig:
    model: Literal[
        "openai-gpt-4-turbo",
        "openai-gpt-3.5-turbo",
        "mistral-mixtral-8x22b",
        "mistral-mixtral-7x8b",
        "mistral-mistral-7b",
        "mistral-small",
        "mistral-large",
        "groq-llama2-70b",
        "groq-mixtral-7x8b",
        "groq-gemma-7b",
        "idk",
    ]
    mode: Literal["chat", "search"]
    max_messages: int
    max_messages_with_context: int
    output_note: Optional[str]
    no_json_schema: bool
    use_emojis: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AnswerConfig":
        return cls(
            model=data["model"],
            mode=data["mode"],
            max_messages=data["max_messages"],
            max_messages_with_context=data["max_messages_with_context"],
            output_note=data["output_note"] if "output_note" in data else None,
            no_json_schema=data["no_json_schema"],
            use_emojis=data["use_emojis"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["model"] = self.model
        data["mode"] = self.mode
        data["max_messages"] = self.max_messages
        data["max_messages_with_context"] = self.max_messages_with_context

        if self.output_note is not None:
            data["output_note"] = self.output_note

        data["no_json_schema"] = self.no_json_schema
        data["use_emojis"] = self.use_emojis

        return data

    @classmethod
    def example(cls) -> "AnswerConfig":
        return cls(
            model="mistral-mistral-7b",
            mode="search",
            max_messages=420,
            max_messages_with_context=420,
            output_note=None,
            no_json_schema=True,
            use_emojis=True,
        )


@dataclass
class RetrieveConfig:
    top_k: int
    augment_question: bool
    augment_question_n: int
    augment_question_merge_method: Literal["concat"]
    augment_question_model: Literal["openai"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RetrieveConfig":
        return cls(
            top_k=data["top_k"],
            augment_question=data["augment_question"],
            augment_question_n=data["augment_question_n"],
            augment_question_merge_method=data["augment_question_merge_method"],
            augment_question_model=data["augment_question_model"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["top_k"] = self.top_k
        data["augment_question"] = self.augment_question
        data["augment_question_n"] = self.augment_question_n
        data["augment_question_merge_method"] = self.augment_question_merge_method
        data["augment_question_model"] = self.augment_question_model

        return data

    @classmethod
    def example(cls) -> "RetrieveConfig":
        return cls(
            top_k=420,
            augment_question=False,
            augment_question_n=666,
            augment_question_merge_method="concat",
            augment_question_model="openai",
        )


@dataclass
class RerankConfig:
    top_k: int
    merge_method: Literal["hit_count"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RerankConfig":
        return cls(
            top_k=data["top_k"],
            merge_method=data["merge_method"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["top_k"] = self.top_k
        data["merge_method"] = self.merge_method

        return data

    @classmethod
    def example(cls) -> "RerankConfig":
        return cls(
            top_k=420,
            merge_method="hit_count",
        )


@dataclass
class CreateAnswerRequest:
    question: str
    build_name: str
    question_id: Optional[int]
    keywords: Optional[list[str]]
    answer_config: Optional[AnswerConfig]
    retrieve_config: Optional[RetrieveConfig]
    rerank_config: Optional[RerankConfig]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateAnswerRequest":
        return cls(
            question=data["question"],
            build_name=data["build_name"],
            question_id=data["question_id"] if "question_id" in data else None,
            keywords=data["keywords"] if "keywords" in data else None,
            answer_config=data["answer_config"] if "answer_config" in data else None,
            retrieve_config=(
                data["retrieve_config"] if "retrieve_config" in data else None
            ),
            rerank_config=data["rerank_config"] if "rerank_config" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["question"] = self.question
        data["build_name"] = self.build_name

        if self.question_id is not None:
            data["question_id"] = self.question_id

        if self.keywords is not None:
            data["keywords"] = self.keywords

        if self.answer_config is not None:
            data["answer_config"] = self.answer_config

        if self.retrieve_config is not None:
            data["retrieve_config"] = self.retrieve_config

        if self.rerank_config is not None:
            data["rerank_config"] = self.rerank_config

        return data

    @classmethod
    def example(cls) -> "CreateAnswerRequest":
        return cls(
            question="The only thing your eyes haven't told me is your name 👀🤔",
            build_name="Just like a fine wine, you get better with age 🍷👵",
            question_id=None,
            keywords=[
                "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
                "The only thing your eyes haven't told me is your name 👀🤔",
                "You've got character! ㍼🥴",
                "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            ],
            answer_config=None,
            retrieve_config=None,
            rerank_config=RerankConfig.example(),
        )


@dataclass
class SearchResultItem:
    item_id: int
    url: Optional[str]
    filename: Optional[str]
    name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "SearchResultItem":
        return cls(
            item_id=data["item_id"],
            url=data["url"] if "url" in data else None,
            filename=data["filename"] if "filename" in data else None,
            name=data["name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["item_id"] = self.item_id

        if self.url is not None:
            data["url"] = self.url

        if self.filename is not None:
            data["filename"] = self.filename

        data["name"] = self.name

        return data

    @classmethod
    def example(cls) -> "SearchResultItem":
        return cls(
            item_id=420,
            url="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            filename=None,
            name="Hi, its kayoc here 😉💅",
        )


@dataclass
class SearchResultSource:
    source_id: int
    build_source_id: int
    search_source_id: int
    item: SearchResultItem

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "SearchResultSource":
        return cls(
            source_id=data["source_id"],
            build_source_id=data["build_source_id"],
            search_source_id=data["search_source_id"],
            item=SearchResultItem.from_json(data["item"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["source_id"] = self.source_id
        data["build_source_id"] = self.build_source_id
        data["search_source_id"] = self.search_source_id
        data["item"] = self.item.to_json()

        return data

    @classmethod
    def example(cls) -> "SearchResultSource":
        return cls(
            source_id=69,
            build_source_id=420,
            search_source_id=69,
            item=SearchResultItem.example(),
        )


@dataclass
class SearchResultResponse:
    search_id: int
    augmented_questions: Optional[list[str]]
    sources: list[SearchResultSource]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "SearchResultResponse":
        return cls(
            search_id=data["search_id"],
            augmented_questions=(
                data["augmented_questions"] if "augmented_questions" in data else None
            ),
            sources=[SearchResultSource.from_json(item) for item in data["sources"]],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["search_id"] = self.search_id

        if self.augmented_questions is not None:
            data["augmented_questions"] = self.augmented_questions

        data["sources"] = [SearchResultSource.to_json(item) for item in self.sources]

        return data

    @classmethod
    def example(cls) -> "SearchResultResponse":
        return cls(
            search_id=420,
            augmented_questions=None,
            sources=[
                SearchResultSource.example(),
                SearchResultSource.example(),
                SearchResultSource.example(),
                SearchResultSource.example(),
                SearchResultSource.example(),
                SearchResultSource.example(),
                SearchResultSource.example(),
            ],
        )


@dataclass
class CreateAnswerResponse:
    answer: str
    quotes: list[str]
    explanation: str
    question_id: int
    answer_id: int
    message_id: int
    search_result: SearchResultResponse
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateAnswerResponse":
        return cls(
            answer=data["answer"],
            quotes=data["quotes"],
            explanation=data["explanation"],
            question_id=data["question_id"],
            answer_id=data["answer_id"],
            message_id=data["message_id"],
            search_result=SearchResultResponse.from_json(data["search_result"]),
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["answer"] = self.answer
        data["quotes"] = self.quotes
        data["explanation"] = self.explanation
        data["question_id"] = self.question_id
        data["answer_id"] = self.answer_id
        data["message_id"] = self.message_id
        data["search_result"] = self.search_result.to_json()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateAnswerResponse":
        return cls(
            answer="The only thing your eyes haven't told me is your name 👀🤔",
            quotes=[
                "Hi, its kayoc here 😉💅",
                "You've got character! ㍼🥴",
                "The only thing your eyes haven't told me is your name 👀🤔",
                "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            ],
            explanation="Wanna go out? No strings attached 🍆🍑",
            question_id=420,
            answer_id=420,
            message_id=69,
            search_result=SearchResultResponse.example(),
            succes=False,
            message="You've got character! ㍼🥴",
            done=False,
        )


@dataclass
class CreateAnswerUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    info: Optional[str]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateAnswerUpdateResponse":
        return cls(
            task=data["task"],
            total=data["total"] if "total" in data else None,
            count=data["count"] if "count" in data else None,
            info=data["info"] if "info" in data else None,
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["task"] = self.task

        if self.total is not None:
            data["total"] = self.total

        if self.count is not None:
            data["count"] = self.count

        if self.info is not None:
            data["info"] = self.info

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateAnswerUpdateResponse":
        return cls(
            task="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            total=666,
            count=None,
            info=None,
            succes=True,
            message="Hi, its kayoc here 😉💅",
            done=True,
        )


@dataclass
class AnswerInfoRequest:
    answer_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AnswerInfoRequest":
        return cls(
            answer_id=data["answer_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["answer_id"] = self.answer_id

        return data

    @classmethod
    def example(cls) -> "AnswerInfoRequest":
        return cls(
            answer_id=666,
        )


@dataclass
class AnswerInfoRating:
    user_name: str
    user_id: int
    rating: Literal["down", "neutral", "up"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AnswerInfoRating":
        return cls(
            user_name=data["user_name"],
            user_id=data["user_id"],
            rating=data["rating"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["user_name"] = self.user_name
        data["user_id"] = self.user_id
        data["rating"] = self.rating

        return data

    @classmethod
    def example(cls) -> "AnswerInfoRating":
        return cls(
            user_name="I'm not a photographer, but I can picture us together 📸👫",
            user_id=69,
            rating="neutral",
        )


@dataclass
class AnswerInfoSourceRating:
    user_name: str
    user_id: int
    rating: Literal["relevant", "irrelevant", "neutral", "click"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AnswerInfoSourceRating":
        return cls(
            user_name=data["user_name"],
            user_id=data["user_id"],
            rating=data["rating"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["user_name"] = self.user_name
        data["user_id"] = self.user_id
        data["rating"] = self.rating

        return data

    @classmethod
    def example(cls) -> "AnswerInfoSourceRating":
        return cls(
            user_name="I'm not a photographer, but I can picture us together 📸👫",
            user_id=666,
            rating="neutral",
        )


@dataclass
class AnswerInfoSource:
    source_id: int
    search_source_id: int
    build_source_id: int
    item_id: int
    content: str
    ratings: list[AnswerInfoSourceRating]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AnswerInfoSource":
        return cls(
            source_id=data["source_id"],
            search_source_id=data["search_source_id"],
            build_source_id=data["build_source_id"],
            item_id=data["item_id"],
            content=data["content"],
            ratings=[
                AnswerInfoSourceRating.from_json(item) for item in data["ratings"]
            ],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["source_id"] = self.source_id
        data["search_source_id"] = self.search_source_id
        data["build_source_id"] = self.build_source_id
        data["item_id"] = self.item_id
        data["content"] = self.content
        data["ratings"] = [
            AnswerInfoSourceRating.to_json(item) for item in self.ratings
        ]

        return data

    @classmethod
    def example(cls) -> "AnswerInfoSource":
        return cls(
            source_id=69,
            search_source_id=420,
            build_source_id=420,
            item_id=420,
            content="Hi, its kayoc here 😉💅",
            ratings=[
                AnswerInfoSourceRating.example(),
                AnswerInfoSourceRating.example(),
                AnswerInfoSourceRating.example(),
                AnswerInfoSourceRating.example(),
                AnswerInfoSourceRating.example(),
            ],
        )


@dataclass
class AnswerInfoResponse:
    answer_id: int
    answer: str
    question: str
    context: str
    explanation: str
    ratings: list[AnswerInfoRating]
    question_id: int
    question_name: str
    message_id: int
    build_id: int
    sources: list[AnswerInfoSource]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AnswerInfoResponse":
        return cls(
            answer_id=data["answer_id"],
            answer=data["answer"],
            question=data["question"],
            context=data["context"],
            explanation=data["explanation"],
            ratings=[AnswerInfoRating.from_json(item) for item in data["ratings"]],
            question_id=data["question_id"],
            question_name=data["question_name"],
            message_id=data["message_id"],
            build_id=data["build_id"],
            sources=[AnswerInfoSource.from_json(item) for item in data["sources"]],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["answer_id"] = self.answer_id
        data["answer"] = self.answer
        data["question"] = self.question
        data["context"] = self.context
        data["explanation"] = self.explanation
        data["ratings"] = [AnswerInfoRating.to_json(item) for item in self.ratings]
        data["question_id"] = self.question_id
        data["question_name"] = self.question_name
        data["message_id"] = self.message_id
        data["build_id"] = self.build_id
        data["sources"] = [AnswerInfoSource.to_json(item) for item in self.sources]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "AnswerInfoResponse":
        return cls(
            answer_id=420,
            answer="Hi, its kayoc here 😉💅",
            question="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            context="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            explanation="You've got character! ㍼🥴",
            ratings=[AnswerInfoRating.example()],
            question_id=69,
            question_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            message_id=666,
            build_id=69,
            sources=[
                AnswerInfoSource.example(),
                AnswerInfoSource.example(),
                AnswerInfoSource.example(),
                AnswerInfoSource.example(),
                AnswerInfoSource.example(),
            ],
            succes=False,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=True,
        )


@dataclass
class RateAnswerRequest:
    rating: Literal["down", "neutral", "up"]
    answer_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RateAnswerRequest":
        return cls(
            rating=data["rating"],
            answer_id=data["answer_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["rating"] = self.rating
        data["answer_id"] = self.answer_id

        return data

    @classmethod
    def example(cls) -> "RateAnswerRequest":
        return cls(
            rating="neutral",
            answer_id=420,
        )


@dataclass
class RateAnswerResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RateAnswerResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RateAnswerResponse":
        return cls(
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )


@dataclass
class AddItemRequest:
    filename: str
    filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"]
    database_name: str
    folder_id: Optional[int]
    is_public: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AddItemRequest":
        return cls(
            filename=data["filename"],
            filetype=data["filetype"],
            database_name=data["database_name"],
            folder_id=data["folder_id"] if "folder_id" in data else None,
            is_public=data["is_public"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["filename"] = self.filename
        data["filetype"] = self.filetype
        data["database_name"] = self.database_name

        if self.folder_id is not None:
            data["folder_id"] = self.folder_id

        data["is_public"] = self.is_public

        return data

    @classmethod
    def example(cls) -> "AddItemRequest":
        return cls(
            filename="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            filetype="docx",
            database_name="Just like a fine wine, you get better with age 🍷👵",
            folder_id=None,
            is_public=True,
        )


@dataclass
class AddItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "AddItemResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "AddItemResponse":
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )


@dataclass
class ItemInfoRequest:
    database_item_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ItemInfoRequest":
        return cls(
            database_item_id=data["database_item_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_item_id"] = self.database_item_id

        return data

    @classmethod
    def example(cls) -> "ItemInfoRequest":
        return cls(
            database_item_id=420,
        )


@dataclass
class ItemInfoFolder:
    name: str
    folder_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ItemInfoFolder":
        return cls(
            name=data["name"],
            folder_id=data["folder_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["name"] = self.name
        data["folder_id"] = self.folder_id

        return data

    @classmethod
    def example(cls) -> "ItemInfoFolder":
        return cls(
            name="The only thing your eyes haven't told me is your name 👀🤔",
            folder_id=420,
        )


@dataclass
class ItemLink:
    file_name: Optional[str]
    url: Optional[str]
    database_item_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ItemLink":
        return cls(
            file_name=data["file_name"] if "file_name" in data else None,
            url=data["url"] if "url" in data else None,
            database_item_id=data["database_item_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.file_name is not None:
            data["file_name"] = self.file_name

        if self.url is not None:
            data["url"] = self.url

        data["database_item_id"] = self.database_item_id

        return data

    @classmethod
    def example(cls) -> "ItemLink":
        return cls(
            file_name=None,
            url="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            database_item_id=69,
        )


@dataclass
class MissingItemLink:
    file_name: Optional[str]
    url: Optional[str]
    item_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "MissingItemLink":
        return cls(
            file_name=data["file_name"] if "file_name" in data else None,
            url=data["url"] if "url" in data else None,
            item_id=data["item_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.file_name is not None:
            data["file_name"] = self.file_name

        if self.url is not None:
            data["url"] = self.url

        data["item_id"] = self.item_id

        return data

    @classmethod
    def example(cls) -> "MissingItemLink":
        return cls(
            file_name=None,
            url="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            item_id=666,
        )


@dataclass
class ItemInfoResponse:
    database_item_id: int
    item_id: int
    name: str
    file_name: Optional[str]
    type: str
    database_folder: ItemInfoFolder
    url: Optional[str]
    outgoing_links: list[ItemLink]
    incoming_links: list[ItemLink]
    missing_incoming_links: list[MissingItemLink]
    missing_outgoing_links: list[MissingItemLink]
    storage_name: Optional[str]
    created_at: DateTime
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ItemInfoResponse":
        return cls(
            database_item_id=data["database_item_id"],
            item_id=data["item_id"],
            name=data["name"],
            file_name=data["file_name"] if "file_name" in data else None,
            type=data["type"],
            database_folder=ItemInfoFolder.from_json(data["database_folder"]),
            url=data["url"] if "url" in data else None,
            outgoing_links=[
                ItemLink.from_json(item) for item in data["outgoing_links"]
            ],
            incoming_links=[
                ItemLink.from_json(item) for item in data["incoming_links"]
            ],
            missing_incoming_links=[
                MissingItemLink.from_json(item)
                for item in data["missing_incoming_links"]
            ],
            missing_outgoing_links=[
                MissingItemLink.from_json(item)
                for item in data["missing_outgoing_links"]
            ],
            storage_name=data["storage_name"] if "storage_name" in data else None,
            created_at=DateTime.from_json(data["created_at"]),
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_item_id"] = self.database_item_id
        data["item_id"] = self.item_id
        data["name"] = self.name

        if self.file_name is not None:
            data["file_name"] = self.file_name

        data["type"] = self.type
        data["database_folder"] = self.database_folder.to_json()

        if self.url is not None:
            data["url"] = self.url

        data["outgoing_links"] = [
            ItemLink.to_json(item) for item in self.outgoing_links
        ]
        data["incoming_links"] = [
            ItemLink.to_json(item) for item in self.incoming_links
        ]
        data["missing_incoming_links"] = [
            MissingItemLink.to_json(item) for item in self.missing_incoming_links
        ]
        data["missing_outgoing_links"] = [
            MissingItemLink.to_json(item) for item in self.missing_outgoing_links
        ]

        if self.storage_name is not None:
            data["storage_name"] = self.storage_name

        data["created_at"] = self.created_at.to_json()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "ItemInfoResponse":
        return cls(
            database_item_id=666,
            item_id=420,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            file_name=None,
            type="I'm not a photographer, but I can picture us together 📸👫",
            database_folder=ItemInfoFolder.example(),
            url=None,
            outgoing_links=[
                ItemLink.example(),
                ItemLink.example(),
                ItemLink.example(),
                ItemLink.example(),
            ],
            incoming_links=[ItemLink.example()],
            missing_incoming_links=[
                MissingItemLink.example(),
                MissingItemLink.example(),
                MissingItemLink.example(),
                MissingItemLink.example(),
            ],
            missing_outgoing_links=[
                MissingItemLink.example(),
                MissingItemLink.example(),
                MissingItemLink.example(),
            ],
            storage_name=None,
            created_at=DateTime.example(),
            succes=True,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=False,
        )


@dataclass
class DeleteItemRequest:
    database_item_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteItemRequest":
        return cls(
            database_item_id=data["database_item_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_item_id"] = self.database_item_id

        return data

    @classmethod
    def example(cls) -> "DeleteItemRequest":
        return cls(
            database_item_id=69,
        )


@dataclass
class DeleteItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteItemResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DeleteItemResponse":
        return cls(
            succes=True,
            message="Hi, its kayoc here 😉💅",
            done=True,
        )


@dataclass
class RenameItemRequest:
    database_item_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameItemRequest":
        return cls(
            database_item_id=data["database_item_id"],
            new_name=data["new_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_item_id"] = self.database_item_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> "RenameItemRequest":
        return cls(
            database_item_id=666,
            new_name="You've got character! ㍼🥴",
        )


@dataclass
class RenameItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameItemResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RenameItemResponse":
        return cls(
            succes=False,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )


@dataclass
class MoveItemRequest:
    database_item_id: int
    new_database_folder_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "MoveItemRequest":
        return cls(
            database_item_id=data["database_item_id"],
            new_database_folder_id=data["new_database_folder_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_item_id"] = self.database_item_id
        data["new_database_folder_id"] = self.new_database_folder_id

        return data

    @classmethod
    def example(cls) -> "MoveItemRequest":
        return cls(
            database_item_id=69,
            new_database_folder_id=420,
        )


@dataclass
class MoveItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "MoveItemResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "MoveItemResponse":
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )


@dataclass
class EmbedConfig:
    blur: bool
    blur_reach: int
    model: Literal[
        "openai-text-embedding-3-small",
        "openai-text-embedding-3-large",
        "mistral-mistral-embed",
        "random",
    ]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "EmbedConfig":
        return cls(
            blur=data["blur"],
            blur_reach=data["blur_reach"],
            model=data["model"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["blur"] = self.blur
        data["blur_reach"] = self.blur_reach
        data["model"] = self.model

        return data

    @classmethod
    def example(cls) -> "EmbedConfig":
        return cls(
            blur=True,
            blur_reach=420,
            model="openai-text-embedding-3-small",
        )


@dataclass
class SourceConfig:
    chunk_size: int
    chunk_overlap: int
    embed_config: EmbedConfig

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "SourceConfig":
        return cls(
            chunk_size=data["chunk_size"],
            chunk_overlap=data["chunk_overlap"],
            embed_config=EmbedConfig.from_json(data["embed_config"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["chunk_size"] = self.chunk_size
        data["chunk_overlap"] = self.chunk_overlap
        data["embed_config"] = self.embed_config.to_json()

        return data

    @classmethod
    def example(cls) -> "SourceConfig":
        return cls(
            chunk_size=420,
            chunk_overlap=69,
            embed_config=EmbedConfig.example(),
        )


@dataclass
class BuildConfig:
    version: Literal["amsterdam", "berlijn"]
    vectorstore_type: Literal["chromastore"]
    source_config: SourceConfig

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildConfig":
        return cls(
            version=data["version"],
            vectorstore_type=data["vectorstore_type"],
            source_config=SourceConfig.from_json(data["source_config"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["version"] = self.version
        data["vectorstore_type"] = self.vectorstore_type
        data["source_config"] = self.source_config.to_json()

        return data

    @classmethod
    def example(cls) -> "BuildConfig":
        return cls(
            version="amsterdam",
            vectorstore_type="chromastore",
            source_config=SourceConfig.example(),
        )


@dataclass
class BuildRequest:
    database_ids: Optional[list[int]]
    database_names: Optional[list[str]]
    build_name: str
    build_config: Optional[BuildConfig]
    background: Optional[bool]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildRequest":
        return cls(
            database_ids=data["database_ids"] if "database_ids" in data else None,
            database_names=data["database_names"] if "database_names" in data else None,
            build_name=data["build_name"],
            build_config=data["build_config"] if "build_config" in data else None,
            background=data["background"] if "background" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.database_ids is not None:
            data["database_ids"] = self.database_ids

        if self.database_names is not None:
            data["database_names"] = self.database_names

        data["build_name"] = self.build_name

        if self.build_config is not None:
            data["build_config"] = self.build_config

        if self.background is not None:
            data["background"] = self.background

        return data

    @classmethod
    def example(cls) -> "BuildRequest":
        return cls(
            database_ids=None,
            database_names=[
                "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
                "The only thing your eyes haven't told me is your name 👀🤔",
                "You've got character! ㍼🥴",
                "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            ],
            build_name="Hi, its kayoc here 😉💅",
            build_config=None,
            background=None,
        )


@dataclass
class BuildStatsErrors:
    unknown_location_types: int
    not_in_storage: int
    not_gotten_from_storage: int
    empty_items: int
    pdf_read_errors: int
    mistral_embed_errors: int
    openai_embed_errors: int
    embed_tasks_not_finished: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildStatsErrors":
        return cls(
            unknown_location_types=data["unknown_location_types"],
            not_in_storage=data["not_in_storage"],
            not_gotten_from_storage=data["not_gotten_from_storage"],
            empty_items=data["empty_items"],
            pdf_read_errors=data["pdf_read_errors"],
            mistral_embed_errors=data["mistral_embed_errors"],
            openai_embed_errors=data["openai_embed_errors"],
            embed_tasks_not_finished=data["embed_tasks_not_finished"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["unknown_location_types"] = self.unknown_location_types
        data["not_in_storage"] = self.not_in_storage
        data["not_gotten_from_storage"] = self.not_gotten_from_storage
        data["empty_items"] = self.empty_items
        data["pdf_read_errors"] = self.pdf_read_errors
        data["mistral_embed_errors"] = self.mistral_embed_errors
        data["openai_embed_errors"] = self.openai_embed_errors
        data["embed_tasks_not_finished"] = self.embed_tasks_not_finished

        return data

    @classmethod
    def example(cls) -> "BuildStatsErrors":
        return cls(
            unknown_location_types=69,
            not_in_storage=69,
            not_gotten_from_storage=420,
            empty_items=69,
            pdf_read_errors=69,
            mistral_embed_errors=666,
            openai_embed_errors=666,
            embed_tasks_not_finished=420,
        )


@dataclass
class BuildStats:
    items_already_in_build: int
    items_after_build: int
    new_items_found: int
    new_items_built: int
    n_errors: int
    errors: BuildStatsErrors

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildStats":
        return cls(
            items_already_in_build=data["items_already_in_build"],
            items_after_build=data["items_after_build"],
            new_items_found=data["new_items_found"],
            new_items_built=data["new_items_built"],
            n_errors=data["n_errors"],
            errors=BuildStatsErrors.from_json(data["errors"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["items_already_in_build"] = self.items_already_in_build
        data["items_after_build"] = self.items_after_build
        data["new_items_found"] = self.new_items_found
        data["new_items_built"] = self.new_items_built
        data["n_errors"] = self.n_errors
        data["errors"] = self.errors.to_json()

        return data

    @classmethod
    def example(cls) -> "BuildStats":
        return cls(
            items_already_in_build=420,
            items_after_build=69,
            new_items_found=666,
            new_items_built=420,
            n_errors=420,
            errors=BuildStatsErrors.example(),
        )


@dataclass
class BuildResponse:
    stats: Optional[BuildStats]
    build_id: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildResponse":
        return cls(
            stats=data["stats"] if "stats" in data else None,
            build_id=data["build_id"],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.stats is not None:
            data["stats"] = self.stats

        data["build_id"] = self.build_id
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "BuildResponse":
        return cls(
            stats=None,
            build_id=666,
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )


@dataclass
class BuildUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildUpdateResponse":
        return cls(
            task=data["task"],
            total=data["total"] if "total" in data else None,
            count=data["count"] if "count" in data else None,
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["task"] = self.task

        if self.total is not None:
            data["total"] = self.total

        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "BuildUpdateResponse":
        return cls(
            task="You've got character! ㍼🥴",
            total=666,
            count=None,
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )


@dataclass
class UpdateBuildRequest:
    build_id: int
    background: Optional[bool]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateBuildRequest":
        return cls(
            build_id=data["build_id"],
            background=data["background"] if "background" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id

        if self.background is not None:
            data["background"] = self.background

        return data

    @classmethod
    def example(cls) -> "UpdateBuildRequest":
        return cls(
            build_id=69,
            background=True,
        )


@dataclass
class UpdateBuildResponse:
    stats: Optional[BuildStats]
    build_id: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateBuildResponse":
        return cls(
            stats=data["stats"] if "stats" in data else None,
            build_id=data["build_id"],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.stats is not None:
            data["stats"] = self.stats

        data["build_id"] = self.build_id
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateBuildResponse":
        return cls(
            stats=BuildStats.example(),
            build_id=69,
            succes=False,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=True,
        )


@dataclass
class UpdateBuildUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateBuildUpdateResponse":
        return cls(
            task=data["task"],
            total=data["total"] if "total" in data else None,
            count=data["count"] if "count" in data else None,
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["task"] = self.task

        if self.total is not None:
            data["total"] = self.total

        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateBuildUpdateResponse":
        return cls(
            task="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            total=None,
            count=None,
            succes=True,
            message="Hi, its kayoc here 😉💅",
            done=False,
        )


@dataclass
class RenameBuildRequest:
    build_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameBuildRequest":
        return cls(
            build_id=data["build_id"],
            new_name=data["new_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> "RenameBuildRequest":
        return cls(
            build_id=69,
            new_name="Just like a fine wine, you get better with age 🍷👵",
        )


@dataclass
class RenameBuildResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameBuildResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RenameBuildResponse":
        return cls(
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )


@dataclass
class DeleteBuildRequest:
    build_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteBuildRequest":
        return cls(
            build_id=data["build_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id

        return data

    @classmethod
    def example(cls) -> "DeleteBuildRequest":
        return cls(
            build_id=69,
        )


@dataclass
class DeleteBuildResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteBuildResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DeleteBuildResponse":
        return cls(
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=False,
        )


@dataclass
class BuildInfoRequest:
    build_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildInfoRequest":
        return cls(
            build_id=data["build_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id

        return data

    @classmethod
    def example(cls) -> "BuildInfoRequest":
        return cls(
            build_id=69,
        )


@dataclass
class BuildInfoDatabase:
    database_id: int
    database_name: str
    database_description: Optional[str]
    n_items: int
    size_bytes: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildInfoDatabase":
        return cls(
            database_id=data["database_id"],
            database_name=data["database_name"],
            database_description=(
                data["database_description"] if "database_description" in data else None
            ),
            n_items=data["n_items"],
            size_bytes=data["size_bytes"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["database_name"] = self.database_name

        if self.database_description is not None:
            data["database_description"] = self.database_description

        data["n_items"] = self.n_items
        data["size_bytes"] = self.size_bytes

        return data

    @classmethod
    def example(cls) -> "BuildInfoDatabase":
        return cls(
            database_id=666,
            database_name="Hi, its kayoc here 😉💅",
            database_description=None,
            n_items=420,
            size_bytes=69,
        )


@dataclass
class BuildInfoQuestion:
    question_id: int
    first_message: str
    name: Optional[str]
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildInfoQuestion":
        return cls(
            question_id=data["question_id"],
            first_message=data["first_message"],
            name=data["name"] if "name" in data else None,
            created_at=DateTime.from_json(data["created_at"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["question_id"] = self.question_id
        data["first_message"] = self.first_message

        if self.name is not None:
            data["name"] = self.name

        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> "BuildInfoQuestion":
        return cls(
            question_id=420,
            first_message="You've got character! ㍼🥴",
            name=None,
            created_at=DateTime.example(),
        )


@dataclass
class BuildInfoStatus:
    message: str
    error: Optional[str]
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildInfoStatus":
        return cls(
            message=data["message"],
            error=data["error"] if "error" in data else None,
            created_at=DateTime.from_json(data["created_at"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["message"] = self.message

        if self.error is not None:
            data["error"] = self.error

        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> "BuildInfoStatus":
        return cls(
            message="I'm not a photographer, but I can picture us together 📸👫",
            error="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            created_at=DateTime.example(),
        )


@dataclass
class BuildInfoResponse:
    build_id: int
    name: str
    created_at: DateTime
    databases: list[BuildInfoDatabase]
    question: list[BuildInfoQuestion]
    statusses: list[BuildInfoStatus]
    nitems: int
    datastore_size_bytes: Optional[int]
    size_bytes: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildInfoResponse":
        return cls(
            build_id=data["build_id"],
            name=data["name"],
            created_at=DateTime.from_json(data["created_at"]),
            databases=[BuildInfoDatabase.from_json(item) for item in data["databases"]],
            question=[BuildInfoQuestion.from_json(item) for item in data["question"]],
            statusses=[BuildInfoStatus.from_json(item) for item in data["statusses"]],
            nitems=data["nitems"],
            datastore_size_bytes=(
                data["datastore_size_bytes"] if "datastore_size_bytes" in data else None
            ),
            size_bytes=data["size_bytes"],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id
        data["name"] = self.name
        data["created_at"] = self.created_at.to_json()
        data["databases"] = [BuildInfoDatabase.to_json(item) for item in self.databases]
        data["question"] = [BuildInfoQuestion.to_json(item) for item in self.question]
        data["statusses"] = [BuildInfoStatus.to_json(item) for item in self.statusses]
        data["nitems"] = self.nitems

        if self.datastore_size_bytes is not None:
            data["datastore_size_bytes"] = self.datastore_size_bytes

        data["size_bytes"] = self.size_bytes
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "BuildInfoResponse":
        return cls(
            build_id=666,
            name="The only thing your eyes haven't told me is your name 👀🤔",
            created_at=DateTime.example(),
            databases=[
                BuildInfoDatabase.example(),
                BuildInfoDatabase.example(),
                BuildInfoDatabase.example(),
                BuildInfoDatabase.example(),
                BuildInfoDatabase.example(),
            ],
            question=[BuildInfoQuestion.example(), BuildInfoQuestion.example()],
            statusses=[BuildInfoStatus.example(), BuildInfoStatus.example()],
            nitems=69,
            datastore_size_bytes=None,
            size_bytes=666,
            succes=True,
            message="You've got character! ㍼🥴",
            done=False,
        )


@dataclass
class BuildListDatabase:
    database_id: int
    database_name: str
    database_description: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildListDatabase":
        return cls(
            database_id=data["database_id"],
            database_name=data["database_name"],
            database_description=(
                data["database_description"] if "database_description" in data else None
            ),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["database_name"] = self.database_name

        if self.database_description is not None:
            data["database_description"] = self.database_description

        return data

    @classmethod
    def example(cls) -> "BuildListDatabase":
        return cls(
            database_id=666,
            database_name="Wanna go out? No strings attached 🍆🍑",
            database_description=None,
        )


@dataclass
class BuildListBuild:
    build_id: int
    build_name: str
    databases: list[BuildListDatabase]
    created_at: DateTime
    nitems: Optional[int]
    datastore_size_bytes: Optional[int]
    size_bytes: Optional[int]
    permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildListBuild":
        return cls(
            build_id=data["build_id"],
            build_name=data["build_name"],
            databases=[BuildListDatabase.from_json(item) for item in data["databases"]],
            created_at=DateTime.from_json(data["created_at"]),
            nitems=data["nitems"] if "nitems" in data else None,
            datastore_size_bytes=(
                data["datastore_size_bytes"] if "datastore_size_bytes" in data else None
            ),
            size_bytes=data["size_bytes"] if "size_bytes" in data else None,
            permission=data["permission"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id
        data["build_name"] = self.build_name
        data["databases"] = [BuildListDatabase.to_json(item) for item in self.databases]
        data["created_at"] = self.created_at.to_json()

        if self.nitems is not None:
            data["nitems"] = self.nitems

        if self.datastore_size_bytes is not None:
            data["datastore_size_bytes"] = self.datastore_size_bytes

        if self.size_bytes is not None:
            data["size_bytes"] = self.size_bytes

        data["permission"] = self.permission

        return data

    @classmethod
    def example(cls) -> "BuildListBuild":
        return cls(
            build_id=420,
            build_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            databases=[
                BuildListDatabase.example(),
                BuildListDatabase.example(),
                BuildListDatabase.example(),
                BuildListDatabase.example(),
                BuildListDatabase.example(),
            ],
            created_at=DateTime.example(),
            nitems=666,
            datastore_size_bytes=666,
            size_bytes=None,
            permission="owner",
        )


@dataclass
class BuildListResponse:
    builds: list[BuildListBuild]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildListResponse":
        return cls(
            builds=[BuildListBuild.from_json(item) for item in data["builds"]],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["builds"] = [BuildListBuild.to_json(item) for item in self.builds]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "BuildListResponse":
        return cls(
            builds=[
                BuildListBuild.example(),
                BuildListBuild.example(),
                BuildListBuild.example(),
                BuildListBuild.example(),
            ],
            succes=False,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=True,
        )


@dataclass
class UpdateBuildPermissionRequest:
    build_id: int
    user_id: int
    new_permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateBuildPermissionRequest":
        return cls(
            build_id=data["build_id"],
            user_id=data["user_id"],
            new_permission=data["new_permission"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id
        data["user_id"] = self.user_id
        data["new_permission"] = self.new_permission

        return data

    @classmethod
    def example(cls) -> "UpdateBuildPermissionRequest":
        return cls(
            build_id=420,
            user_id=666,
            new_permission="owner",
        )


@dataclass
class UpdateBuildPermissionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateBuildPermissionResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateBuildPermissionResponse":
        return cls(
            succes=False,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=True,
        )


@dataclass
class BuildSourceInfoRequest:
    build_source_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildSourceInfoRequest":
        return cls(
            build_source_id=data["build_source_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_source_id"] = self.build_source_id

        return data

    @classmethod
    def example(cls) -> "BuildSourceInfoRequest":
        return cls(
            build_source_id=666,
        )


@dataclass
class BuildSourceInfoResponse:
    source_id: int
    build_id: int
    build_source_id: int
    build_item_id: int
    item_id: int
    type: Literal["text"]
    text: Optional[str]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BuildSourceInfoResponse":
        return cls(
            source_id=data["source_id"],
            build_id=data["build_id"],
            build_source_id=data["build_source_id"],
            build_item_id=data["build_item_id"],
            item_id=data["item_id"],
            type=data["type"],
            text=data["text"] if "text" in data else None,
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["source_id"] = self.source_id
        data["build_id"] = self.build_id
        data["build_source_id"] = self.build_source_id
        data["build_item_id"] = self.build_item_id
        data["item_id"] = self.item_id
        data["type"] = self.type

        if self.text is not None:
            data["text"] = self.text

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "BuildSourceInfoResponse":
        return cls(
            source_id=666,
            build_id=666,
            build_source_id=69,
            build_item_id=69,
            item_id=420,
            type="text",
            text=None,
            succes=False,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )


@dataclass
class CreateUserRequest:
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    company: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateUserRequest":
        return cls(
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"] if "first_name" in data else None,
            last_name=data["last_name"] if "last_name" in data else None,
            company=data["company"] if "company" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["email"] = self.email
        data["password"] = self.password

        if self.first_name is not None:
            data["first_name"] = self.first_name

        if self.last_name is not None:
            data["last_name"] = self.last_name

        if self.company is not None:
            data["company"] = self.company

        return data

    @classmethod
    def example(cls) -> "CreateUserRequest":
        return cls(
            email="Wanna go out? No strings attached 🍆🍑",
            password="Wanna go out? No strings attached 🍆🍑",
            first_name=None,
            last_name=None,
            company="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )


@dataclass
class CreateUserResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateUserResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateUserResponse":
        return cls(
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )


@dataclass
class LoginRequest:
    email: str
    password: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "LoginRequest":
        return cls(
            email=data["email"],
            password=data["password"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["email"] = self.email
        data["password"] = self.password

        return data

    @classmethod
    def example(cls) -> "LoginRequest":
        return cls(
            email="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            password="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
        )


@dataclass
class LoginResponse:
    succes: bool
    message: str
    done: bool
    user_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "LoginResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
            user_id=data["user_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["user_id"] = self.user_id

        return data

    @classmethod
    def example(cls) -> "LoginResponse":
        return cls(
            succes=True,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
            user_id=420,
        )


@dataclass
class LogoutResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "LogoutResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "LogoutResponse":
        return cls(
            succes=False,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )


@dataclass
class OAuthRequest:
    provider: Literal["twitter", "google", "github", "facebook"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "OAuthRequest":
        return cls(
            provider=data["provider"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["provider"] = self.provider

        return data

    @classmethod
    def example(cls) -> "OAuthRequest":
        return cls(
            provider="google",
        )


@dataclass
class OAuthResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "OAuthResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "OAuthResponse":
        return cls(
            succes=False,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=False,
        )


@dataclass
class OAuthAuthorizeRequest:
    provider: Literal["twitter", "google", "github", "facebook"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "OAuthAuthorizeRequest":
        return cls(
            provider=data["provider"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["provider"] = self.provider

        return data

    @classmethod
    def example(cls) -> "OAuthAuthorizeRequest":
        return cls(
            provider="facebook",
        )


@dataclass
class OAuthAuthorizeResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "OAuthAuthorizeResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "OAuthAuthorizeResponse":
        return cls(
            succes=False,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )


@dataclass
class BirthDay:
    day: int
    month: int
    year: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "BirthDay":
        return cls(
            day=data["day"],
            month=data["month"],
            year=data["year"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["day"] = self.day
        data["month"] = self.month
        data["year"] = self.year

        return data

    @classmethod
    def example(cls) -> "BirthDay":
        return cls(
            day=420,
            month=69,
            year=420,
        )


@dataclass
class UpdateProfileRequest:
    first_name: Optional[str]
    last_name: Optional[str]
    company: Optional[str]
    birthday: Optional[BirthDay]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateProfileRequest":
        return cls(
            first_name=data["first_name"] if "first_name" in data else None,
            last_name=data["last_name"] if "last_name" in data else None,
            company=data["company"] if "company" in data else None,
            birthday=data["birthday"] if "birthday" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.first_name is not None:
            data["first_name"] = self.first_name

        if self.last_name is not None:
            data["last_name"] = self.last_name

        if self.company is not None:
            data["company"] = self.company

        if self.birthday is not None:
            data["birthday"] = self.birthday

        return data

    @classmethod
    def example(cls) -> "UpdateProfileRequest":
        return cls(
            first_name=None,
            last_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            company=None,
            birthday=None,
        )


@dataclass
class UpdateProfileResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateProfileResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateProfileResponse":
        return cls(
            succes=False,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=False,
        )


@dataclass
class UserProfile:
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[BirthDay]
    company: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UserProfile":
        return cls(
            first_name=data["first_name"] if "first_name" in data else None,
            last_name=data["last_name"] if "last_name" in data else None,
            birthday=data["birthday"] if "birthday" in data else None,
            company=data["company"] if "company" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.first_name is not None:
            data["first_name"] = self.first_name

        if self.last_name is not None:
            data["last_name"] = self.last_name

        if self.birthday is not None:
            data["birthday"] = self.birthday

        if self.company is not None:
            data["company"] = self.company

        return data

    @classmethod
    def example(cls) -> "UserProfile":
        return cls(
            first_name=None,
            last_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            birthday=None,
            company="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )


@dataclass
class UserDatabase:
    database_id: int
    name: str
    permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UserDatabase":
        return cls(
            database_id=data["database_id"],
            name=data["name"],
            permission=data["permission"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name
        data["permission"] = self.permission

        return data

    @classmethod
    def example(cls) -> "UserDatabase":
        return cls(
            database_id=69,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            permission="read",
        )


@dataclass
class UserBuild:
    build_id: int
    name: str
    permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UserBuild":
        return cls(
            build_id=data["build_id"],
            name=data["name"],
            permission=data["permission"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["build_id"] = self.build_id
        data["name"] = self.name
        data["permission"] = self.permission

        return data

    @classmethod
    def example(cls) -> "UserBuild":
        return cls(
            build_id=69,
            name="Hi, its kayoc here 😉💅",
            permission="write",
        )


@dataclass
class UserApiToken:
    token_id: int
    user_id: int
    name: str
    created_at: DateTime
    last_used_at: Optional[DateTime]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UserApiToken":
        return cls(
            token_id=data["token_id"],
            user_id=data["user_id"],
            name=data["name"],
            created_at=DateTime.from_json(data["created_at"]),
            last_used_at=data["last_used_at"] if "last_used_at" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["token_id"] = self.token_id
        data["user_id"] = self.user_id
        data["name"] = self.name
        data["created_at"] = self.created_at.to_json()

        if self.last_used_at is not None:
            data["last_used_at"] = self.last_used_at

        return data

    @classmethod
    def example(cls) -> "UserApiToken":
        return cls(
            token_id=69,
            user_id=69,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            created_at=DateTime.example(),
            last_used_at=DateTime.example(),
        )


@dataclass
class UserInfoResponse:
    user_id: int
    email: str
    created_at: DateTime
    profile: UserProfile
    databases: list[UserDatabase]
    builds: list[UserBuild]
    tokens: list[UserApiToken]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UserInfoResponse":
        return cls(
            user_id=data["user_id"],
            email=data["email"],
            created_at=DateTime.from_json(data["created_at"]),
            profile=UserProfile.from_json(data["profile"]),
            databases=[UserDatabase.from_json(item) for item in data["databases"]],
            builds=[UserBuild.from_json(item) for item in data["builds"]],
            tokens=[UserApiToken.from_json(item) for item in data["tokens"]],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["user_id"] = self.user_id
        data["email"] = self.email
        data["created_at"] = self.created_at.to_json()
        data["profile"] = self.profile.to_json()
        data["databases"] = [UserDatabase.to_json(item) for item in self.databases]
        data["builds"] = [UserBuild.to_json(item) for item in self.builds]
        data["tokens"] = [UserApiToken.to_json(item) for item in self.tokens]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UserInfoResponse":
        return cls(
            user_id=69,
            email="Wanna go out? No strings attached 🍆🍑",
            created_at=DateTime.example(),
            profile=UserProfile.example(),
            databases=[UserDatabase.example()],
            builds=[
                UserBuild.example(),
                UserBuild.example(),
                UserBuild.example(),
                UserBuild.example(),
                UserBuild.example(),
            ],
            tokens=[UserApiToken.example()],
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )


@dataclass
class UpdatePasswordRequest:
    new_password: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdatePasswordRequest":
        return cls(
            new_password=data["new_password"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["new_password"] = self.new_password

        return data

    @classmethod
    def example(cls) -> "UpdatePasswordRequest":
        return cls(
            new_password="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
        )


@dataclass
class UpdatePasswordResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdatePasswordResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdatePasswordResponse":
        return cls(
            succes=True,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=True,
        )


@dataclass
class UpdateEmailRequest:
    new_email: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateEmailRequest":
        return cls(
            new_email=data["new_email"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["new_email"] = self.new_email

        return data

    @classmethod
    def example(cls) -> "UpdateEmailRequest":
        return cls(
            new_email="Wanna go out? No strings attached 🍆🍑",
        )


@dataclass
class UpdateEmailResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateEmailResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateEmailResponse":
        return cls(
            succes=False,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )


@dataclass
class DeleteUserResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteUserResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DeleteUserResponse":
        return cls(
            succes=True,
            message="You've got character! ㍼🥴",
            done=True,
        )


@dataclass
class TokenDatabasePermission:
    permission: Literal["read", "write", "delete", "admin", "owner"]
    database_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "TokenDatabasePermission":
        return cls(
            permission=data["permission"],
            database_id=data["database_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["permission"] = self.permission
        data["database_id"] = self.database_id

        return data

    @classmethod
    def example(cls) -> "TokenDatabasePermission":
        return cls(
            permission="read",
            database_id=69,
        )


@dataclass
class TokenBuildPermission:
    permission: Literal["read", "write", "delete", "admin", "owner"]
    build_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "TokenBuildPermission":
        return cls(
            permission=data["permission"],
            build_id=data["build_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["permission"] = self.permission
        data["build_id"] = self.build_id

        return data

    @classmethod
    def example(cls) -> "TokenBuildPermission":
        return cls(
            permission="admin",
            build_id=69,
        )


@dataclass
class CreateTokenRequest:
    name: str
    user_permission: Optional[Literal["read", "write", "delete"]]
    database_permissions: Optional[list[TokenDatabasePermission]]
    build_permission: Optional[list[TokenBuildPermission]]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateTokenRequest":
        return cls(
            name=data["name"],
            user_permission=(
                data["user_permission"] if "user_permission" in data else None
            ),
            database_permissions=(
                data["database_permissions"] if "database_permissions" in data else None
            ),
            build_permission=(
                data["build_permission"] if "build_permission" in data else None
            ),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["name"] = self.name

        if self.user_permission is not None:
            data["user_permission"] = self.user_permission

        if self.database_permissions is not None:
            data["database_permissions"] = self.database_permissions

        if self.build_permission is not None:
            data["build_permission"] = self.build_permission

        return data

    @classmethod
    def example(cls) -> "CreateTokenRequest":
        return cls(
            name="The only thing your eyes haven't told me is your name 👀🤔",
            user_permission="read",
            database_permissions=None,
            build_permission=None,
        )


@dataclass
class CreateTokenResponse:
    token: str
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateTokenResponse":
        return cls(
            token=data["token"],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["token"] = self.token
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateTokenResponse":
        return cls(
            token="Wanna go out? No strings attached 🍆🍑",
            succes=False,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=False,
        )


@dataclass
class DeleteFolderRequest:
    database_folder_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteFolderRequest":
        return cls(
            database_folder_id=data["database_folder_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_folder_id"] = self.database_folder_id

        return data

    @classmethod
    def example(cls) -> "DeleteFolderRequest":
        return cls(
            database_folder_id=420,
        )


@dataclass
class DeleteFolderResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DeleteFolderResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DeleteFolderResponse":
        return cls(
            succes=False,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=True,
        )


@dataclass
class RenameFolderRequest:
    folder_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameFolderRequest":
        return cls(
            folder_id=data["folder_id"],
            new_name=data["new_name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> "RenameFolderRequest":
        return cls(
            folder_id=69,
            new_name="You've got character! ㍼🥴",
        )


@dataclass
class RenameFolderResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RenameFolderResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RenameFolderResponse":
        return cls(
            succes=False,
            message="Hi, its kayoc here 😉💅",
            done=False,
        )


@dataclass
class UpdateFolderDescriptionRequest:
    folder_id: int
    new_description: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateFolderDescriptionRequest":
        return cls(
            folder_id=data["folder_id"],
            new_description=data["new_description"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id
        data["new_description"] = self.new_description

        return data

    @classmethod
    def example(cls) -> "UpdateFolderDescriptionRequest":
        return cls(
            folder_id=666,
            new_description="The only thing your eyes haven't told me is your name 👀🤔",
        )


@dataclass
class UpdateFolderDescriptionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "UpdateFolderDescriptionResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "UpdateFolderDescriptionResponse":
        return cls(
            succes=False,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )


@dataclass
class DatabaseFolderInfoRequest:
    folder_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseFolderInfoRequest":
        return cls(
            folder_id=data["folder_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id

        return data

    @classmethod
    def example(cls) -> "DatabaseFolderInfoRequest":
        return cls(
            folder_id=666,
        )


@dataclass
class FoldeInfoSubFolder:
    folder_id: int
    name: str
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "FoldeInfoSubFolder":
        return cls(
            folder_id=data["folder_id"],
            name=data["name"],
            description=data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name

        if self.description is not None:
            data["description"] = self.description

        return data

    @classmethod
    def example(cls) -> "FoldeInfoSubFolder":
        return cls(
            folder_id=666,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            description="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )


@dataclass
class FolderItemInfo:
    item_id: int
    name: str
    type: str
    url: Optional[str]
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "FolderItemInfo":
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            type=data["type"],
            url=data["url"] if "url" in data else None,
            created_at=DateTime.from_json(data["created_at"]),
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["item_id"] = self.item_id
        data["name"] = self.name
        data["type"] = self.type

        if self.url is not None:
            data["url"] = self.url

        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> "FolderItemInfo":
        return cls(
            item_id=69,
            name="Hi, its kayoc here 😉💅",
            type="The only thing your eyes haven't told me is your name 👀🤔",
            url=None,
            created_at=DateTime.example(),
        )


@dataclass
class DatabaseFolderInfoResponse:
    folder_id: int
    name: str
    description: Optional[str]
    created_at: DateTime
    subfolders: list[FoldeInfoSubFolder]
    items: list[FolderItemInfo]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "DatabaseFolderInfoResponse":
        return cls(
            folder_id=data["folder_id"],
            name=data["name"],
            description=data["description"] if "description" in data else None,
            created_at=DateTime.from_json(data["created_at"]),
            subfolders=[
                FoldeInfoSubFolder.from_json(item) for item in data["subfolders"]
            ],
            items=[FolderItemInfo.from_json(item) for item in data["items"]],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name

        if self.description is not None:
            data["description"] = self.description

        data["created_at"] = self.created_at.to_json()
        data["subfolders"] = [
            FoldeInfoSubFolder.to_json(item) for item in self.subfolders
        ]
        data["items"] = [FolderItemInfo.to_json(item) for item in self.items]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "DatabaseFolderInfoResponse":
        return cls(
            folder_id=420,
            name="The only thing your eyes haven't told me is your name 👀🤔",
            description="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            created_at=DateTime.example(),
            subfolders=[
                FoldeInfoSubFolder.example(),
                FoldeInfoSubFolder.example(),
                FoldeInfoSubFolder.example(),
                FoldeInfoSubFolder.example(),
            ],
            items=[
                FolderItemInfo.example(),
                FolderItemInfo.example(),
                FolderItemInfo.example(),
                FolderItemInfo.example(),
                FolderItemInfo.example(),
                FolderItemInfo.example(),
                FolderItemInfo.example(),
            ],
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )


@dataclass
class ScrapeConfig:
    allow_external_links: bool
    load_dynamic: bool
    timeout_seconds: int
    max_pages: Optional[int]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeConfig":
        return cls(
            allow_external_links=data["allow_external_links"],
            load_dynamic=data["load_dynamic"],
            timeout_seconds=data["timeout_seconds"],
            max_pages=data["max_pages"] if "max_pages" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["allow_external_links"] = self.allow_external_links
        data["load_dynamic"] = self.load_dynamic
        data["timeout_seconds"] = self.timeout_seconds

        if self.max_pages is not None:
            data["max_pages"] = self.max_pages

        return data

    @classmethod
    def example(cls) -> "ScrapeConfig":
        return cls(
            allow_external_links=True,
            load_dynamic=True,
            timeout_seconds=69,
            max_pages=666,
        )


@dataclass
class ScrapeRequest:
    urls: list[str]
    database_name: str
    scrape_config: Optional[ScrapeConfig]
    depths: Optional[list[int]]
    folder_path: Optional[list[str]]
    background: Optional[bool]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeRequest":
        return cls(
            urls=data["urls"],
            database_name=data["database_name"],
            scrape_config=data["scrape_config"] if "scrape_config" in data else None,
            depths=data["depths"] if "depths" in data else None,
            folder_path=data["folder_path"] if "folder_path" in data else None,
            background=data["background"] if "background" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["urls"] = self.urls
        data["database_name"] = self.database_name

        if self.scrape_config is not None:
            data["scrape_config"] = self.scrape_config

        if self.depths is not None:
            data["depths"] = self.depths

        if self.folder_path is not None:
            data["folder_path"] = self.folder_path

        if self.background is not None:
            data["background"] = self.background

        return data

    @classmethod
    def example(cls) -> "ScrapeRequest":
        return cls(
            urls=[
                "The only thing your eyes haven't told me is your name 👀🤔",
                "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
                "You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            ],
            database_name="Hi, its kayoc here 😉💅",
            scrape_config=ScrapeConfig.example(),
            depths=None,
            folder_path=None,
            background=None,
        )


@dataclass
class ScrapeResponse:
    succes: bool
    message: str
    done: bool
    nitems: int
    nerror: int
    nskip: int
    nlink: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
            nitems=data["nitems"],
            nerror=data["nerror"],
            nskip=data["nskip"],
            nlink=data["nlink"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["nitems"] = self.nitems
        data["nerror"] = self.nerror
        data["nskip"] = self.nskip
        data["nlink"] = self.nlink

        return data

    @classmethod
    def example(cls) -> "ScrapeResponse":
        return cls(
            succes=True,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=False,
            nitems=666,
            nerror=666,
            nskip=420,
            nlink=69,
        )


@dataclass
class ScrapeUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeUpdateResponse":
        return cls(
            task=data["task"],
            total=data["total"] if "total" in data else None,
            count=data["count"] if "count" in data else None,
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["task"] = self.task

        if self.total is not None:
            data["total"] = self.total

        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "ScrapeUpdateResponse":
        return cls(
            task="The only thing your eyes haven't told me is your name 👀🤔",
            total=None,
            count=None,
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=True,
        )


@dataclass
class ScrapeInfoRequest:
    scrape_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeInfoRequest":
        return cls(
            scrape_id=data["scrape_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["scrape_id"] = self.scrape_id

        return data

    @classmethod
    def example(cls) -> "ScrapeInfoRequest":
        return cls(
            scrape_id=666,
        )


@dataclass
class ScrapeDatabase:
    database_id: int
    name: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeDatabase":
        return cls(
            database_id=data["database_id"],
            name=data["name"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name

        return data

    @classmethod
    def example(cls) -> "ScrapeDatabase":
        return cls(
            database_id=666,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
        )


@dataclass
class ScrapeItem:
    url: Optional[str]
    type: str
    name: str
    folder: str
    folder_id: int
    item_id: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeItem":
        return cls(
            url=data["url"] if "url" in data else None,
            type=data["type"],
            name=data["name"],
            folder=data["folder"],
            folder_id=data["folder_id"],
            item_id=data["item_id"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()

        if self.url is not None:
            data["url"] = self.url

        data["type"] = self.type
        data["name"] = self.name
        data["folder"] = self.folder
        data["folder_id"] = self.folder_id
        data["item_id"] = self.item_id

        return data

    @classmethod
    def example(cls) -> "ScrapeItem":
        return cls(
            url="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            type="Wanna go out? No strings attached 🍆🍑",
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            folder="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            folder_id=666,
            item_id=69,
        )


@dataclass
class ScrapeInfoResponse:
    scrape_id: int
    created_at: DateTime
    database: ScrapeDatabase
    items: list[ScrapeItem]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "ScrapeInfoResponse":
        return cls(
            scrape_id=data["scrape_id"],
            created_at=DateTime.from_json(data["created_at"]),
            database=ScrapeDatabase.from_json(data["database"]),
            items=[ScrapeItem.from_json(item) for item in data["items"]],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["scrape_id"] = self.scrape_id
        data["created_at"] = self.created_at.to_json()
        data["database"] = self.database.to_json()
        data["items"] = [ScrapeItem.to_json(item) for item in self.items]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "ScrapeInfoResponse":
        return cls(
            scrape_id=666,
            created_at=DateTime.example(),
            database=ScrapeDatabase.example(),
            items=[
                ScrapeItem.example(),
                ScrapeItem.example(),
                ScrapeItem.example(),
                ScrapeItem.example(),
                ScrapeItem.example(),
                ScrapeItem.example(),
                ScrapeItem.example(),
            ],
            succes=False,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )


@dataclass
class CreateSearchRequest:
    question: str
    build_name: str
    keywords: Optional[list[str]]
    retrieve_config: Optional[RetrieveConfig]
    rerank_config: Optional[RerankConfig]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateSearchRequest":
        return cls(
            question=data["question"],
            build_name=data["build_name"],
            keywords=data["keywords"] if "keywords" in data else None,
            retrieve_config=(
                data["retrieve_config"] if "retrieve_config" in data else None
            ),
            rerank_config=data["rerank_config"] if "rerank_config" in data else None,
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["question"] = self.question
        data["build_name"] = self.build_name

        if self.keywords is not None:
            data["keywords"] = self.keywords

        if self.retrieve_config is not None:
            data["retrieve_config"] = self.retrieve_config

        if self.rerank_config is not None:
            data["rerank_config"] = self.rerank_config

        return data

    @classmethod
    def example(cls) -> "CreateSearchRequest":
        return cls(
            question="I'm not a photographer, but I can picture us together 📸👫",
            build_name="Just like a fine wine, you get better with age 🍷👵",
            keywords=[
                "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
                "The only thing your eyes haven't told me is your name 👀🤔",
                "You've got character! ㍼🥴",
                "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            ],
            retrieve_config=None,
            rerank_config=RerankConfig.example(),
        )


@dataclass
class CreateSearchResponse:
    search_id: int
    augmented_questions: Optional[list[str]]
    sources: list[SearchResultSource]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateSearchResponse":
        return cls(
            search_id=data["search_id"],
            augmented_questions=(
                data["augmented_questions"] if "augmented_questions" in data else None
            ),
            sources=[SearchResultSource.from_json(item) for item in data["sources"]],
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["search_id"] = self.search_id

        if self.augmented_questions is not None:
            data["augmented_questions"] = self.augmented_questions

        data["sources"] = [SearchResultSource.to_json(item) for item in self.sources]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateSearchResponse":
        return cls(
            search_id=420,
            augmented_questions=[
                "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
                "The only thing your eyes haven't told me is your name 👀🤔",
                "You've got character! ㍼🥴",
                "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            ],
            sources=[SearchResultSource.example(), SearchResultSource.example()],
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=False,
        )


@dataclass
class CreateSearchUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    info: Optional[str]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "CreateSearchUpdateResponse":
        return cls(
            task=data["task"],
            total=data["total"] if "total" in data else None,
            count=data["count"] if "count" in data else None,
            info=data["info"] if "info" in data else None,
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["task"] = self.task

        if self.total is not None:
            data["total"] = self.total

        if self.count is not None:
            data["count"] = self.count

        if self.info is not None:
            data["info"] = self.info

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "CreateSearchUpdateResponse":
        return cls(
            task="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            total=None,
            count=None,
            info=None,
            succes=False,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )


@dataclass
class RateSearchRequest:
    search_id: int
    rating: Literal["down", "neutral", "up"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RateSearchRequest":
        return cls(
            search_id=data["search_id"],
            rating=data["rating"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["search_id"] = self.search_id
        data["rating"] = self.rating

        return data

    @classmethod
    def example(cls) -> "RateSearchRequest":
        return cls(
            search_id=420,
            rating="down",
        )


@dataclass
class RateSearchResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RateSearchResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RateSearchResponse":
        return cls(
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )


@dataclass
class RateSearchSourceRequest:
    search_source_id: int
    rating: Literal["relevant", "irrelevant", "neutral", "click"]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RateSearchSourceRequest":
        return cls(
            search_source_id=data["search_source_id"],
            rating=data["rating"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["search_source_id"] = self.search_source_id
        data["rating"] = self.rating

        return data

    @classmethod
    def example(cls) -> "RateSearchSourceRequest":
        return cls(
            search_source_id=420,
            rating="irrelevant",
        )


@dataclass
class RateSearchSourceResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "RateSearchSourceResponse":
        return cls(
            succes=data["succes"],
            message=data["message"],
            done=data["done"],
        )

    def to_json(self) -> dict[str, Any]:
        data: dict[str, Any] = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> "RateSearchSourceResponse":
        return cls(
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=False,
        )


import requests
import aiohttp

import os
import json
from typing import Optional, Generator, AsyncGenerator, Union
import random
from io import BytesIO
import asyncio


class KayocApi:

    def __init__(
        self,
        api_key: Optional[str] = None,
        session: Optional[requests.Session] = None,
        base_url: Optional[str] = None,
    ) -> None:
        self.session = requests.Session() if session is None else session
        self.base_url = (
            "https://api.kayoc.vancerefrigeration.nl"
            if base_url is None
            else base_url.rstrip("/")
        )
        self.api_key = os.environ.get("KAYOC_API_KEY") if api_key is None else api_key

        if self.api_key is not None:
            self.session.headers.update({"Authorization": "Bearer " + self.api_key})

    def __repr__(self) -> str:
        return "{}({})".format(KayocApi, self.base_url)

    def __str__(self) -> str:
        return "{}({})".format(KayocApi, self.base_url)

    def close(self) -> None:
        self.session.close()

    def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/create"
            data = CreateDatabaseRequest(database_name=database_name).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return CreateDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/delete"
            data = DeleteDatabaseRequest(database_name=database_name).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_info(
        self, database_name: Optional[str] = None, database_id: Optional[int] = None
    ) -> Union[DatabaseInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/info"
            data = DatabaseInfoRequest(
                database_name=database_name, database_id=database_id
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_rename(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/rename"
            data = RenameDatabaseRequest(
                database_name=database_name, new_name=new_name
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_redescribe(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/redescribe"
            data = DatabaseUpdateDescriptionRequest(
                database_name=database_name, new_description=new_description
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseUpdateDescriptionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        try:
            url = self.base_url + "/database/browse"
            data = DatabaseBrowseRequest(
                fuzzy_database_name=fuzzy_database_name
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseBrowseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_user(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        try:
            url = self.base_url + "/database/user"
            data = DatabaseUpdatePermissionRequest(
                database_name=database_name,
                user_email=user_email,
                new_permission=new_permission,
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseUpdatePermissionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/publish"
            data = PublishDatabaseRequest(database_name=database_name).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return PublishDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/unpublish"
            data = UnpublishDatabaseRequest(database_name=database_name).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UnpublishDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        try:
            url = self.base_url + "/database/list"
            data = None

            files = None

            response = self.session.get(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseListResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        try:
            url = self.base_url + "/question/info"
            data = QuestionInfoRequest(question_id=question_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return QuestionInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        try:
            url = self.base_url + "/question/list"
            data = None

            files = None

            response = self.session.get(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return QuestionListResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def question_rename(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        try:
            url = self.base_url + "/question/rename"
            data = UpdateQuestionNameRequest(
                question_id=question_id, new_name=new_name
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateQuestionNameResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def answer_create(
        self,
        question: str,
        build_name: str,
        question_id: Optional[int] = None,
        keywords: Optional[list[str]] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> Generator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None, None
    ]:

        url = self.base_url + "/answer/create"
        data = CreateAnswerRequest(
            question=question,
            build_name=build_name,
            question_id=question_id,
            keywords=keywords,
            answer_config=answer_config,
            retrieve_config=retrieve_config,
            rerank_config=rerank_config,
        ).to_json()

        files = None

        try:
            response = self.session.post(url, json=data, files=files, stream=True)

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield CreateAnswerResponse.from_json(update)
                    return
                else:
                    yield CreateAnswerUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def answer_info(self, answer_id: int) -> Union[AnswerInfoResponse, KayocError]:
        try:
            url = self.base_url + "/answer/info"
            data = AnswerInfoRequest(answer_id=answer_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return AnswerInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        try:
            url = self.base_url + "/answer/rate"
            data = RateAnswerRequest(rating=rating, answer_id=answer_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RateAnswerResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        is_public: bool,
        file: BytesIO,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/add"
            data = AddItemRequest(
                filename=filename,
                filetype=filetype,
                database_name=database_name,
                folder_id=folder_id,
                is_public=is_public,
            ).to_json()

            files = dict(file=(None, file, "application/octet-stream"))
            data = {"data": json.dumps(data)}

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return AddItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_info(
        self, database_item_id: int
    ) -> Union[ItemInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/info"
            data = ItemInfoRequest(database_item_id=database_item_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return ItemInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_delete(
        self, database_item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/delete"
            data = DeleteItemRequest(database_item_id=database_item_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_rename(
        self, database_item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/rename"
            data = RenameItemRequest(
                database_item_id=database_item_id, new_name=new_name
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_move(
        self, database_item_id: int, new_database_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/move"
            data = MoveItemRequest(
                database_item_id=database_item_id,
                new_database_folder_id=new_database_folder_id,
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return MoveItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def build_create(
        self,
        build_name: str,
        database_ids: Optional[list[int]] = None,
        database_names: Optional[list[str]] = None,
        build_config: Optional[BuildConfig] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[BuildResponse, KayocError, BuildUpdateResponse], None, None]:

        url = self.base_url + "/build/create"
        data = BuildRequest(
            database_ids=database_ids,
            database_names=database_names,
            build_name=build_name,
            build_config=build_config,
            background=background,
        ).to_json()

        files = None

        try:
            response = self.session.post(url, json=data, files=files, stream=True)

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield BuildResponse.from_json(update)
                    return
                else:
                    yield BuildUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def build_update(
        self, build_id: int, background: Optional[bool] = None
    ) -> Generator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None, None
    ]:

        url = self.base_url + "/build/update"
        data = UpdateBuildRequest(build_id=build_id, background=background).to_json()

        files = None

        try:
            response = self.session.post(url, json=data, files=files, stream=True)

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield UpdateBuildResponse.from_json(update)
                    return
                else:
                    yield UpdateBuildUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def build_rename(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        try:
            url = self.base_url + "/build/rename"
            data = RenameBuildRequest(build_id=build_id, new_name=new_name).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameBuildResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def build_delete(self, build_id: int) -> Union[DeleteBuildResponse, KayocError]:
        try:
            url = self.base_url + "/build/delete"
            data = DeleteBuildRequest(build_id=build_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteBuildResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def build_info(self, build_id: int) -> Union[BuildInfoResponse, KayocError]:
        try:
            url = self.base_url + "/build/info"
            data = BuildInfoRequest(build_id=build_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return BuildInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        try:
            url = self.base_url + "/build/list"
            data = None

            files = None

            response = self.session.get(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return BuildListResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def build_user(
        self,
        build_id: int,
        user_id: int,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[UpdateBuildPermissionResponse, KayocError]:
        try:
            url = self.base_url + "/build/user"
            data = UpdateBuildPermissionRequest(
                build_id=build_id, user_id=user_id, new_permission=new_permission
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateBuildPermissionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def build_source_info(
        self, build_source_id: int
    ) -> Union[BuildSourceInfoResponse, KayocError]:
        try:
            url = self.base_url + "/build/source/info"
            data = BuildSourceInfoRequest(build_source_id=build_source_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return BuildSourceInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_create(
        self,
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/create"
            data = CreateUserRequest(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                company=company,
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return CreateUserResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_login(self, email: str, password: str) -> Union[LoginResponse, KayocError]:
        try:
            url = self.base_url + "/user/login"
            data = LoginRequest(email=email, password=password).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return LoginResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        try:
            url = self.base_url + "/user/logout"
            data = None

            files = None

            response = self.session.get(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return LogoutResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/login"
            data = OAuthRequest(provider=provider).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return OAuthResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/authorize"
            data = OAuthAuthorizeRequest(provider=provider).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return OAuthAuthorizeResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        try:
            url = self.base_url + "/user/profile/update"
            data = UpdateProfileRequest(
                first_name=first_name,
                last_name=last_name,
                company=company,
                birthday=birthday,
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateProfileResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        try:
            url = self.base_url + "/user/info"
            data = None

            files = None

            response = self.session.get(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UserInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        try:
            url = self.base_url + "/user/password/update"
            data = UpdatePasswordRequest(new_password=new_password).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdatePasswordResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        try:
            url = self.base_url + "/user/email/update"
            data = UpdateEmailRequest(new_email=new_email).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateEmailResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/delete"
            data = None

            files = None

            response = self.session.get(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteUserResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_token_create(
        self,
        name: str,
        user_permission: Optional[Literal["read", "write", "delete"]] = None,
        database_permissions: Optional[list[TokenDatabasePermission]] = None,
        build_permission: Optional[list[TokenBuildPermission]] = None,
    ) -> Union[CreateTokenResponse, KayocError]:
        try:
            url = self.base_url + "/user/token/create"
            data = CreateTokenRequest(
                name=name,
                user_permission=user_permission,
                database_permissions=database_permissions,
                build_permission=build_permission,
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return CreateTokenResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_folder_delete(
        self, database_folder_id: int
    ) -> Union[DeleteFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/delete"
            data = DeleteFolderRequest(database_folder_id=database_folder_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteFolderResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_folder_rename(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/rename"
            data = RenameFolderRequest(folder_id=folder_id, new_name=new_name).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameFolderResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_folder_redescribe(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/redescribe"
            data = UpdateFolderDescriptionRequest(
                folder_id=folder_id, new_description=new_description
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateFolderDescriptionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_folder_info(
        self, folder_id: int
    ) -> Union[DatabaseFolderInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/info"
            data = DatabaseFolderInfoRequest(folder_id=folder_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseFolderInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_scrape_create(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None, None]:

        url = self.base_url + "/database/scrape/create"
        data = ScrapeRequest(
            urls=urls,
            database_name=database_name,
            scrape_config=scrape_config,
            depths=depths,
            folder_path=folder_path,
            background=background,
        ).to_json()

        files = None

        try:
            response = self.session.post(url, json=data, files=files, stream=True)

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield ScrapeResponse.from_json(update)
                    return
                else:
                    yield ScrapeUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def database_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/scrape/info"
            data = ScrapeInfoRequest(scrape_id=scrape_id).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return ScrapeInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def search_create(
        self,
        question: str,
        build_name: str,
        keywords: Optional[list[str]] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> Generator[
        Union[CreateSearchResponse, KayocError, CreateSearchUpdateResponse], None, None
    ]:

        url = self.base_url + "/search/create"
        data = CreateSearchRequest(
            question=question,
            build_name=build_name,
            keywords=keywords,
            retrieve_config=retrieve_config,
            rerank_config=rerank_config,
        ).to_json()

        files = None

        try:
            response = self.session.post(url, json=data, files=files, stream=True)

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield CreateSearchResponse.from_json(update)
                    return
                else:
                    yield CreateSearchUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def search_rate(
        self, search_id: int, rating: Literal["down", "neutral", "up"]
    ) -> Union[RateSearchResponse, KayocError]:
        try:
            url = self.base_url + "/search/rate"
            data = RateSearchRequest(search_id=search_id, rating=rating).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RateSearchResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def search_source_rate(
        self,
        search_source_id: int,
        rating: Literal["relevant", "irrelevant", "neutral", "click"],
    ) -> Union[RateSearchSourceResponse, KayocError]:
        try:
            url = self.base_url + "/search/source/rate"
            data = RateSearchSourceRequest(
                search_source_id=search_source_id, rating=rating
            ).to_json()

            files = None

            response = self.session.post(url, json=data, files=files)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RateSearchSourceResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )


class KayocApiAsync:

    def __init__(
        self,
        asession: aiohttp.ClientSession,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:

        self.asession = asession
        self.base_url = (
            "https://api.kayoc.vancerefrigeration.nl" if base_url is None else base_url
        )
        self.api_key = os.environ.get("KAYOC_API_KEY") if api_key is None else api_key

        # TODO: add api key header

        raise NotImplementedError(
            "The async client is not working as expected yet. Please use the sync client for now."
        )

    @classmethod
    async def new(
        cls,
        asession: Optional[aiohttp.ClientSession] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> "KayocApiAsync":
        if asession is None:
            asession = aiohttp.ClientSession()

        return KayocApiAsync(asession, api_key, base_url)

        raise NotImplementedError(
            "The async client is not working as expected yet. Please use the sync client for now."
        )

    def __repr__(self) -> str:
        return "{}({})".format(KayocApi, self.base_url)

    def __str__(self) -> str:
        return "{}({})".format(KayocApi, self.base_url)

    async def close(self) -> None:
        await self.asession.close()

    async def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/create"
            async with self.asession.post(
                url, json=CreateDatabaseRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return CreateDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/delete"
            async with self.asession.post(
                url, json=DeleteDatabaseRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_info(
        self, database_name: Optional[str] = None, database_id: Optional[int] = None
    ) -> Union[DatabaseInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/info"
            async with self.asession.post(
                url,
                json=DatabaseInfoRequest(
                    database_name=database_name, database_id=database_id
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_rename(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/rename"
            async with self.asession.post(
                url,
                json=RenameDatabaseRequest(
                    database_name=database_name, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_redescribe(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/redescribe"
            async with self.asession.post(
                url,
                json=DatabaseUpdateDescriptionRequest(
                    database_name=database_name, new_description=new_description
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseUpdateDescriptionResponse.from_json(
                    await response.json()
                )
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        try:
            url = self.base_url + "/database/browse"
            async with self.asession.post(
                url,
                json=DatabaseBrowseRequest(
                    fuzzy_database_name=fuzzy_database_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseBrowseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_user(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        try:
            url = self.base_url + "/database/user"
            async with self.asession.post(
                url,
                json=DatabaseUpdatePermissionRequest(
                    database_name=database_name,
                    user_email=user_email,
                    new_permission=new_permission,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseUpdatePermissionResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/publish"
            async with self.asession.post(
                url, json=PublishDatabaseRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return PublishDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/unpublish"
            async with self.asession.post(
                url,
                json=UnpublishDatabaseRequest(database_name=database_name).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UnpublishDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        try:
            url = self.base_url + "/database/list"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseListResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        try:
            url = self.base_url + "/question/info"
            async with self.asession.post(
                url, json=QuestionInfoRequest(question_id=question_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return QuestionInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        try:
            url = self.base_url + "/question/list"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return QuestionListResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def question_rename(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        try:
            url = self.base_url + "/question/rename"
            async with self.asession.post(
                url,
                json=UpdateQuestionNameRequest(
                    question_id=question_id, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateQuestionNameResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def answer_create(
        self,
        question: str,
        build_name: str,
        question_id: Optional[int] = None,
        keywords: Optional[list[str]] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> AsyncGenerator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None
    ]:
        url = self.base_url + "/answer/create"
        try:
            async with self.asession.post(
                url,
                json=CreateAnswerRequest(
                    question=question,
                    build_name=build_name,
                    question_id=question_id,
                    keywords=keywords,
                    answer_config=answer_config,
                    retrieve_config=retrieve_config,
                    rerank_config=rerank_config,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield CreateAnswerResponse.from_json(update)
                            return
                        else:
                            yield CreateAnswerUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def answer_info(
        self, answer_id: int
    ) -> Union[AnswerInfoResponse, KayocError]:
        try:
            url = self.base_url + "/answer/info"
            async with self.asession.post(
                url, json=AnswerInfoRequest(answer_id=answer_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return AnswerInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        try:
            url = self.base_url + "/answer/rate"
            async with self.asession.post(
                url,
                json=RateAnswerRequest(rating=rating, answer_id=answer_id).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RateAnswerResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        is_public: bool,
        file: BytesIO,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/add"
            async with self.asession.post(
                url,
                json=AddItemRequest(
                    filename=filename,
                    filetype=filetype,
                    database_name=database_name,
                    folder_id=folder_id,
                    is_public=is_public,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return AddItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_info(
        self, database_item_id: int
    ) -> Union[ItemInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/info"
            async with self.asession.post(
                url, json=ItemInfoRequest(database_item_id=database_item_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return ItemInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_delete(
        self, database_item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/delete"
            async with self.asession.post(
                url, json=DeleteItemRequest(database_item_id=database_item_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_rename(
        self, database_item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/rename"
            async with self.asession.post(
                url,
                json=RenameItemRequest(
                    database_item_id=database_item_id, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_move(
        self, database_item_id: int, new_database_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/move"
            async with self.asession.post(
                url,
                json=MoveItemRequest(
                    database_item_id=database_item_id,
                    new_database_folder_id=new_database_folder_id,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return MoveItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_create(
        self,
        build_name: str,
        database_ids: Optional[list[int]] = None,
        database_names: Optional[list[str]] = None,
        build_config: Optional[BuildConfig] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[BuildResponse, KayocError, BuildUpdateResponse], None]:
        url = self.base_url + "/build/create"
        try:
            async with self.asession.post(
                url,
                json=BuildRequest(
                    database_ids=database_ids,
                    database_names=database_names,
                    build_name=build_name,
                    build_config=build_config,
                    background=background,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield BuildResponse.from_json(update)
                            return
                        else:
                            yield BuildUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_update(
        self, build_id: int, background: Optional[bool] = None
    ) -> AsyncGenerator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None
    ]:
        url = self.base_url + "/build/update"
        try:
            async with self.asession.post(
                url,
                json=UpdateBuildRequest(
                    build_id=build_id, background=background
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield UpdateBuildResponse.from_json(update)
                            return
                        else:
                            yield UpdateBuildUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_rename(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        try:
            url = self.base_url + "/build/rename"
            async with self.asession.post(
                url,
                json=RenameBuildRequest(build_id=build_id, new_name=new_name).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameBuildResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_delete(
        self, build_id: int
    ) -> Union[DeleteBuildResponse, KayocError]:
        try:
            url = self.base_url + "/build/delete"
            async with self.asession.post(
                url, json=DeleteBuildRequest(build_id=build_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteBuildResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_info(self, build_id: int) -> Union[BuildInfoResponse, KayocError]:
        try:
            url = self.base_url + "/build/info"
            async with self.asession.post(
                url, json=BuildInfoRequest(build_id=build_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return BuildInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        try:
            url = self.base_url + "/build/list"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return BuildListResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_user(
        self,
        build_id: int,
        user_id: int,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[UpdateBuildPermissionResponse, KayocError]:
        try:
            url = self.base_url + "/build/user"
            async with self.asession.post(
                url,
                json=UpdateBuildPermissionRequest(
                    build_id=build_id, user_id=user_id, new_permission=new_permission
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateBuildPermissionResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def build_source_info(
        self, build_source_id: int
    ) -> Union[BuildSourceInfoResponse, KayocError]:
        try:
            url = self.base_url + "/build/source/info"
            async with self.asession.post(
                url,
                json=BuildSourceInfoRequest(build_source_id=build_source_id).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return BuildSourceInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_create(
        self,
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/create"
            async with self.asession.post(
                url,
                json=CreateUserRequest(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    company=company,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return CreateUserResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_login(
        self, email: str, password: str
    ) -> Union[LoginResponse, KayocError]:
        try:
            url = self.base_url + "/user/login"
            async with self.asession.post(
                url, json=LoginRequest(email=email, password=password).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return LoginResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        try:
            url = self.base_url + "/user/logout"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return LogoutResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/login"
            async with self.asession.post(
                url, json=OAuthRequest(provider=provider).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return OAuthResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/authorize"
            async with self.asession.post(
                url, json=OAuthAuthorizeRequest(provider=provider).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return OAuthAuthorizeResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        try:
            url = self.base_url + "/user/profile/update"
            async with self.asession.post(
                url,
                json=UpdateProfileRequest(
                    first_name=first_name,
                    last_name=last_name,
                    company=company,
                    birthday=birthday,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateProfileResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        try:
            url = self.base_url + "/user/info"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UserInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        try:
            url = self.base_url + "/user/password/update"
            async with self.asession.post(
                url, json=UpdatePasswordRequest(new_password=new_password).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdatePasswordResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        try:
            url = self.base_url + "/user/email/update"
            async with self.asession.post(
                url, json=UpdateEmailRequest(new_email=new_email).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateEmailResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/delete"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteUserResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_token_create(
        self,
        name: str,
        user_permission: Optional[Literal["read", "write", "delete"]] = None,
        database_permissions: Optional[list[TokenDatabasePermission]] = None,
        build_permission: Optional[list[TokenBuildPermission]] = None,
    ) -> Union[CreateTokenResponse, KayocError]:
        try:
            url = self.base_url + "/user/token/create"
            async with self.asession.post(
                url,
                json=CreateTokenRequest(
                    name=name,
                    user_permission=user_permission,
                    database_permissions=database_permissions,
                    build_permission=build_permission,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return CreateTokenResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_folder_delete(
        self, database_folder_id: int
    ) -> Union[DeleteFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/delete"
            async with self.asession.post(
                url,
                json=DeleteFolderRequest(
                    database_folder_id=database_folder_id
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteFolderResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_folder_rename(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/rename"
            async with self.asession.post(
                url,
                json=RenameFolderRequest(
                    folder_id=folder_id, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameFolderResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_folder_redescribe(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/redescribe"
            async with self.asession.post(
                url,
                json=UpdateFolderDescriptionRequest(
                    folder_id=folder_id, new_description=new_description
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateFolderDescriptionResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_folder_info(
        self, folder_id: int
    ) -> Union[DatabaseFolderInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/folder/info"
            async with self.asession.post(
                url, json=DatabaseFolderInfoRequest(folder_id=folder_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseFolderInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_scrape_create(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None]:
        url = self.base_url + "/database/scrape/create"
        try:
            async with self.asession.post(
                url,
                json=ScrapeRequest(
                    urls=urls,
                    database_name=database_name,
                    scrape_config=scrape_config,
                    depths=depths,
                    folder_path=folder_path,
                    background=background,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield ScrapeResponse.from_json(update)
                            return
                        else:
                            yield ScrapeUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/scrape/info"
            async with self.asession.post(
                url, json=ScrapeInfoRequest(scrape_id=scrape_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return ScrapeInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def search_create(
        self,
        question: str,
        build_name: str,
        keywords: Optional[list[str]] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> AsyncGenerator[
        Union[CreateSearchResponse, KayocError, CreateSearchUpdateResponse], None
    ]:
        url = self.base_url + "/search/create"
        try:
            async with self.asession.post(
                url,
                json=CreateSearchRequest(
                    question=question,
                    build_name=build_name,
                    keywords=keywords,
                    retrieve_config=retrieve_config,
                    rerank_config=rerank_config,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield CreateSearchResponse.from_json(update)
                            return
                        else:
                            yield CreateSearchUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def search_rate(
        self, search_id: int, rating: Literal["down", "neutral", "up"]
    ) -> Union[RateSearchResponse, KayocError]:
        try:
            url = self.base_url + "/search/rate"
            async with self.asession.post(
                url,
                json=RateSearchRequest(search_id=search_id, rating=rating).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RateSearchResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def search_source_rate(
        self,
        search_source_id: int,
        rating: Literal["relevant", "irrelevant", "neutral", "click"],
    ) -> Union[RateSearchSourceResponse, KayocError]:
        try:
            url = self.base_url + "/search/source/rate"
            async with self.asession.post(
                url,
                json=RateSearchSourceRequest(
                    search_source_id=search_source_id, rating=rating
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RateSearchSourceResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )


class ExampleKayocApi:

    def __init__(
        self,
        error_rate: float = 0.1,
        max_updates: int = 10,
        stream_error_rate: float = 0.05,
    ):
        self.error_rate = error_rate
        self.max_updates = max_updates
        self.stream_error_rate = stream_error_rate

    def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_info(
        self, database_name: Optional[str] = None, database_id: Optional[int] = None
    ) -> Union[DatabaseInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_rename(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_redescribe(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdateDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseBrowseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_user(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdatePermissionResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = PublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UnpublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseListResponse.example()
        response.done = True
        response.succes = True
        return response

    def question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionListResponse.example()
        response.done = True
        response.succes = True
        return response

    def question_rename(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateQuestionNameResponse.example()
        response.done = True
        response.succes = True
        return response

    def answer_create(
        self,
        question: str,
        build_name: str,
        question_id: Optional[int] = None,
        keywords: Optional[list[str]] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> Generator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None, None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = CreateAnswerUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = CreateAnswerResponse.example()
        response.done = True
        response.succes = True
        yield response

    def answer_info(self, answer_id: int) -> Union[AnswerInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AnswerInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateAnswerResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        is_public: bool,
        file: BytesIO,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AddItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_info(
        self, database_item_id: int
    ) -> Union[ItemInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ItemInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_delete(
        self, database_item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_rename(
        self, database_item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_move(
        self, database_item_id: int, new_database_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = MoveItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def build_create(
        self,
        build_name: str,
        database_ids: Optional[list[int]] = None,
        database_names: Optional[list[str]] = None,
        build_config: Optional[BuildConfig] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[BuildResponse, KayocError, BuildUpdateResponse], None, None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = BuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = BuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    def build_update(
        self, build_id: int, background: Optional[bool] = None
    ) -> Generator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None, None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = UpdateBuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = UpdateBuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    def build_rename(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    def build_delete(self, build_id: int) -> Union[DeleteBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    def build_info(self, build_id: int) -> Union[BuildInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildListResponse.example()
        response.done = True
        response.succes = True
        return response

    def build_user(
        self,
        build_id: int,
        user_id: int,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[UpdateBuildPermissionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateBuildPermissionResponse.example()
        response.done = True
        response.succes = True
        return response

    def build_source_info(
        self, build_source_id: int
    ) -> Union[BuildSourceInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildSourceInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_create(
        self,
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateUserResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_login(self, email: str, password: str) -> Union[LoginResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LoginResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LogoutResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthAuthorizeResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateProfileResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UserInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdatePasswordResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateEmailResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteUserResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_token_create(
        self,
        name: str,
        user_permission: Optional[Literal["read", "write", "delete"]] = None,
        database_permissions: Optional[list[TokenDatabasePermission]] = None,
        build_permission: Optional[list[TokenBuildPermission]] = None,
    ) -> Union[CreateTokenResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateTokenResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_folder_delete(
        self, database_folder_id: int
    ) -> Union[DeleteFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_folder_rename(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_folder_redescribe(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateFolderDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_folder_info(
        self, folder_id: int
    ) -> Union[DatabaseFolderInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseFolderInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_scrape_create(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None, None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = ScrapeUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = ScrapeResponse.example()
        response.done = True
        response.succes = True
        yield response

    def database_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ScrapeInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def search_create(
        self,
        question: str,
        build_name: str,
        keywords: Optional[list[str]] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> Generator[
        Union[CreateSearchResponse, KayocError, CreateSearchUpdateResponse], None, None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = CreateSearchUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = CreateSearchResponse.example()
        response.done = True
        response.succes = True
        yield response

    def search_rate(
        self, search_id: int, rating: Literal["down", "neutral", "up"]
    ) -> Union[RateSearchResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateSearchResponse.example()
        response.done = True
        response.succes = True
        return response

    def search_source_rate(
        self,
        search_source_id: int,
        rating: Literal["relevant", "irrelevant", "neutral", "click"],
    ) -> Union[RateSearchSourceResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateSearchSourceResponse.example()
        response.done = True
        response.succes = True
        return response


class ExampleKayocApiAsync:

    def __init__(
        self,
        error_rate: float = 0.1,
        max_updates: int = 10,
        stream_error_rate: float = 0.05,
    ):
        self.error_rate = error_rate
        self.max_updates = max_updates
        self.stream_error_rate = stream_error_rate

    async def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_info(
        self, database_name: Optional[str] = None, database_id: Optional[int] = None
    ) -> Union[DatabaseInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_rename(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_redescribe(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdateDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseBrowseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_user(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdatePermissionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = PublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UnpublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseListResponse.example()
        response.done = True
        response.succes = True
        return response

    async def question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionListResponse.example()
        response.done = True
        response.succes = True
        return response

    async def question_rename(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateQuestionNameResponse.example()
        response.done = True
        response.succes = True
        return response

    async def answer_create(
        self,
        question: str,
        build_name: str,
        question_id: Optional[int] = None,
        keywords: Optional[list[str]] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> AsyncGenerator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = CreateAnswerUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = CreateAnswerResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def answer_info(
        self, answer_id: int
    ) -> Union[AnswerInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AnswerInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateAnswerResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        is_public: bool,
        file: BytesIO,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AddItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_info(
        self, database_item_id: int
    ) -> Union[ItemInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ItemInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_delete(
        self, database_item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_rename(
        self, database_item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_move(
        self, database_item_id: int, new_database_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = MoveItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def build_create(
        self,
        build_name: str,
        database_ids: Optional[list[int]] = None,
        database_names: Optional[list[str]] = None,
        build_config: Optional[BuildConfig] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[BuildResponse, KayocError, BuildUpdateResponse], None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = BuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = BuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def build_update(
        self, build_id: int, background: Optional[bool] = None
    ) -> AsyncGenerator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = UpdateBuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = UpdateBuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def build_rename(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    async def build_delete(
        self, build_id: int
    ) -> Union[DeleteBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    async def build_info(self, build_id: int) -> Union[BuildInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildListResponse.example()
        response.done = True
        response.succes = True
        return response

    async def build_user(
        self,
        build_id: int,
        user_id: int,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[UpdateBuildPermissionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateBuildPermissionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def build_source_info(
        self, build_source_id: int
    ) -> Union[BuildSourceInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildSourceInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_create(
        self,
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateUserResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_login(
        self, email: str, password: str
    ) -> Union[LoginResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LoginResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LogoutResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthAuthorizeResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateProfileResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UserInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdatePasswordResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateEmailResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteUserResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_token_create(
        self,
        name: str,
        user_permission: Optional[Literal["read", "write", "delete"]] = None,
        database_permissions: Optional[list[TokenDatabasePermission]] = None,
        build_permission: Optional[list[TokenBuildPermission]] = None,
    ) -> Union[CreateTokenResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateTokenResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_folder_delete(
        self, database_folder_id: int
    ) -> Union[DeleteFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_folder_rename(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_folder_redescribe(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateFolderDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_folder_info(
        self, folder_id: int
    ) -> Union[DatabaseFolderInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseFolderInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_scrape_create(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = ScrapeUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = ScrapeResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def database_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ScrapeInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def search_create(
        self,
        question: str,
        build_name: str,
        keywords: Optional[list[str]] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> AsyncGenerator[
        Union[CreateSearchResponse, KayocError, CreateSearchUpdateResponse], None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = CreateSearchUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = CreateSearchResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def search_rate(
        self, search_id: int, rating: Literal["down", "neutral", "up"]
    ) -> Union[RateSearchResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateSearchResponse.example()
        response.done = True
        response.succes = True
        return response

    async def search_source_rate(
        self,
        search_source_id: int,
        rating: Literal["relevant", "irrelevant", "neutral", "click"],
    ) -> Union[RateSearchSourceResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateSearchSourceResponse.example()
        response.done = True
        response.succes = True
        return response
