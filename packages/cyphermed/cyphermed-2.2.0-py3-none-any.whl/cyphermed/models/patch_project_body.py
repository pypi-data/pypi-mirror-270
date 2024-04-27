from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.interface_config import InterfaceConfig


T = TypeVar("T", bound="PatchProjectBody")


@_attrs_define
class PatchProjectBody:
    """Patch project body

    Attributes:
        description (Union[Unset, str]): Description of the project
        is_delete_protected (Union[Unset, bool]): Must be false before the project can be deleted
        tags (Union[Unset, List[str]]): List of tags on this project
        reset_token_expire_hours (Union[Unset, int]): Number of hours reset tokens are valid (1-168)
        access_token_expire_hours (Union[Unset, int]): Number of hours access tokens are valid (1-24)
        refresh_token_expire_hours (Union[Unset, int]): Number of hours refresh tokens are valid (1-8760)
        session_expire_mins (Union[Unset, int]): Number of mins sessions are valid (3-15)
        default_locale (Union[Unset, str]): Default locale for the organization Default: 'en-US'.
        default_from_address (Union[Unset, str]): Default from address Default: 'noreply@cyphermed.cloud'.
        ui_config (Union[Unset, InterfaceConfig]): Configuration for the user interface
        name (Union[Unset, str]): Name of the project
        is_active (Union[Unset, bool]): If false, all project operations are disabled
    """

    description: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    reset_token_expire_hours: Union[Unset, int] = UNSET
    access_token_expire_hours: Union[Unset, int] = UNSET
    refresh_token_expire_hours: Union[Unset, int] = UNSET
    session_expire_mins: Union[Unset, int] = UNSET
    default_locale: Union[Unset, str] = "en-US"
    default_from_address: Union[Unset, str] = "noreply@cyphermed.cloud"
    ui_config: Union[Unset, "InterfaceConfig"] = UNSET
    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        reset_token_expire_hours = self.reset_token_expire_hours

        access_token_expire_hours = self.access_token_expire_hours

        refresh_token_expire_hours = self.refresh_token_expire_hours

        session_expire_mins = self.session_expire_mins

        default_locale = self.default_locale

        default_from_address = self.default_from_address

        ui_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ui_config, Unset):
            ui_config = self.ui_config.to_dict()

        name = self.name

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if reset_token_expire_hours is not UNSET:
            field_dict["reset_token_expire_hours"] = reset_token_expire_hours
        if access_token_expire_hours is not UNSET:
            field_dict["access_token_expire_hours"] = access_token_expire_hours
        if refresh_token_expire_hours is not UNSET:
            field_dict["refresh_token_expire_hours"] = refresh_token_expire_hours
        if session_expire_mins is not UNSET:
            field_dict["session_expire_mins"] = session_expire_mins
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if default_from_address is not UNSET:
            field_dict["default_from_address"] = default_from_address
        if ui_config is not UNSET:
            field_dict["ui_config"] = ui_config
        if name is not UNSET:
            field_dict["name"] = name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_config import InterfaceConfig

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        reset_token_expire_hours = d.pop("reset_token_expire_hours", UNSET)

        access_token_expire_hours = d.pop("access_token_expire_hours", UNSET)

        refresh_token_expire_hours = d.pop("refresh_token_expire_hours", UNSET)

        session_expire_mins = d.pop("session_expire_mins", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        default_from_address = d.pop("default_from_address", UNSET)

        _ui_config = d.pop("ui_config", UNSET)
        ui_config: Union[Unset, InterfaceConfig]
        if isinstance(_ui_config, Unset):
            ui_config = UNSET
        else:
            ui_config = InterfaceConfig.from_dict(_ui_config)

        name = d.pop("name", UNSET)

        is_active = d.pop("is_active", UNSET)

        patch_project_body = cls(
            description=description,
            is_delete_protected=is_delete_protected,
            tags=tags,
            reset_token_expire_hours=reset_token_expire_hours,
            access_token_expire_hours=access_token_expire_hours,
            refresh_token_expire_hours=refresh_token_expire_hours,
            session_expire_mins=session_expire_mins,
            default_locale=default_locale,
            default_from_address=default_from_address,
            ui_config=ui_config,
            name=name,
            is_active=is_active,
        )

        patch_project_body.additional_properties = d
        return patch_project_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
