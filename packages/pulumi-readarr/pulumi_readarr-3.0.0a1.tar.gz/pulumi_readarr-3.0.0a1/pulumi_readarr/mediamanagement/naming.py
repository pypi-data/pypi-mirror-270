# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NamingArgs', 'Naming']

@pulumi.input_type
class NamingArgs:
    def __init__(__self__, *,
                 author_folder_format: pulumi.Input[str],
                 colon_replacement_format: pulumi.Input[int],
                 rename_books: pulumi.Input[bool],
                 replace_illegal_characters: pulumi.Input[bool],
                 standard_book_format: pulumi.Input[str]):
        """
        The set of arguments for constructing a Naming resource.
        :param pulumi.Input[str] author_folder_format: Author folder format.
        :param pulumi.Input[int] colon_replacement_format: Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        :param pulumi.Input[bool] rename_books: Readarr will use the existing file name if false.
        :param pulumi.Input[bool] replace_illegal_characters: Replace illegal characters. They will be removed if false.
        :param pulumi.Input[str] standard_book_format: Standard book formatss.
        """
        pulumi.set(__self__, "author_folder_format", author_folder_format)
        pulumi.set(__self__, "colon_replacement_format", colon_replacement_format)
        pulumi.set(__self__, "rename_books", rename_books)
        pulumi.set(__self__, "replace_illegal_characters", replace_illegal_characters)
        pulumi.set(__self__, "standard_book_format", standard_book_format)

    @property
    @pulumi.getter(name="authorFolderFormat")
    def author_folder_format(self) -> pulumi.Input[str]:
        """
        Author folder format.
        """
        return pulumi.get(self, "author_folder_format")

    @author_folder_format.setter
    def author_folder_format(self, value: pulumi.Input[str]):
        pulumi.set(self, "author_folder_format", value)

    @property
    @pulumi.getter(name="colonReplacementFormat")
    def colon_replacement_format(self) -> pulumi.Input[int]:
        """
        Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        """
        return pulumi.get(self, "colon_replacement_format")

    @colon_replacement_format.setter
    def colon_replacement_format(self, value: pulumi.Input[int]):
        pulumi.set(self, "colon_replacement_format", value)

    @property
    @pulumi.getter(name="renameBooks")
    def rename_books(self) -> pulumi.Input[bool]:
        """
        Readarr will use the existing file name if false.
        """
        return pulumi.get(self, "rename_books")

    @rename_books.setter
    def rename_books(self, value: pulumi.Input[bool]):
        pulumi.set(self, "rename_books", value)

    @property
    @pulumi.getter(name="replaceIllegalCharacters")
    def replace_illegal_characters(self) -> pulumi.Input[bool]:
        """
        Replace illegal characters. They will be removed if false.
        """
        return pulumi.get(self, "replace_illegal_characters")

    @replace_illegal_characters.setter
    def replace_illegal_characters(self, value: pulumi.Input[bool]):
        pulumi.set(self, "replace_illegal_characters", value)

    @property
    @pulumi.getter(name="standardBookFormat")
    def standard_book_format(self) -> pulumi.Input[str]:
        """
        Standard book formatss.
        """
        return pulumi.get(self, "standard_book_format")

    @standard_book_format.setter
    def standard_book_format(self, value: pulumi.Input[str]):
        pulumi.set(self, "standard_book_format", value)


@pulumi.input_type
class _NamingState:
    def __init__(__self__, *,
                 author_folder_format: Optional[pulumi.Input[str]] = None,
                 colon_replacement_format: Optional[pulumi.Input[int]] = None,
                 rename_books: Optional[pulumi.Input[bool]] = None,
                 replace_illegal_characters: Optional[pulumi.Input[bool]] = None,
                 standard_book_format: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Naming resources.
        :param pulumi.Input[str] author_folder_format: Author folder format.
        :param pulumi.Input[int] colon_replacement_format: Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        :param pulumi.Input[bool] rename_books: Readarr will use the existing file name if false.
        :param pulumi.Input[bool] replace_illegal_characters: Replace illegal characters. They will be removed if false.
        :param pulumi.Input[str] standard_book_format: Standard book formatss.
        """
        if author_folder_format is not None:
            pulumi.set(__self__, "author_folder_format", author_folder_format)
        if colon_replacement_format is not None:
            pulumi.set(__self__, "colon_replacement_format", colon_replacement_format)
        if rename_books is not None:
            pulumi.set(__self__, "rename_books", rename_books)
        if replace_illegal_characters is not None:
            pulumi.set(__self__, "replace_illegal_characters", replace_illegal_characters)
        if standard_book_format is not None:
            pulumi.set(__self__, "standard_book_format", standard_book_format)

    @property
    @pulumi.getter(name="authorFolderFormat")
    def author_folder_format(self) -> Optional[pulumi.Input[str]]:
        """
        Author folder format.
        """
        return pulumi.get(self, "author_folder_format")

    @author_folder_format.setter
    def author_folder_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "author_folder_format", value)

    @property
    @pulumi.getter(name="colonReplacementFormat")
    def colon_replacement_format(self) -> Optional[pulumi.Input[int]]:
        """
        Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        """
        return pulumi.get(self, "colon_replacement_format")

    @colon_replacement_format.setter
    def colon_replacement_format(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "colon_replacement_format", value)

    @property
    @pulumi.getter(name="renameBooks")
    def rename_books(self) -> Optional[pulumi.Input[bool]]:
        """
        Readarr will use the existing file name if false.
        """
        return pulumi.get(self, "rename_books")

    @rename_books.setter
    def rename_books(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "rename_books", value)

    @property
    @pulumi.getter(name="replaceIllegalCharacters")
    def replace_illegal_characters(self) -> Optional[pulumi.Input[bool]]:
        """
        Replace illegal characters. They will be removed if false.
        """
        return pulumi.get(self, "replace_illegal_characters")

    @replace_illegal_characters.setter
    def replace_illegal_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace_illegal_characters", value)

    @property
    @pulumi.getter(name="standardBookFormat")
    def standard_book_format(self) -> Optional[pulumi.Input[str]]:
        """
        Standard book formatss.
        """
        return pulumi.get(self, "standard_book_format")

    @standard_book_format.setter
    def standard_book_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "standard_book_format", value)


class Naming(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author_folder_format: Optional[pulumi.Input[str]] = None,
                 colon_replacement_format: Optional[pulumi.Input[int]] = None,
                 rename_books: Optional[pulumi.Input[bool]] = None,
                 replace_illegal_characters: Optional[pulumi.Input[bool]] = None,
                 standard_book_format: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Media Management -->Naming resource.
        For more information refer to [Naming](https://wiki.servarr.com/readarr/settings#community-naming-suggestions) documentation.

        ## Import

        import does not need parameters

        ```sh
         $ pulumi import readarr:MediaManagement/naming:Naming example ""
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] author_folder_format: Author folder format.
        :param pulumi.Input[int] colon_replacement_format: Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        :param pulumi.Input[bool] rename_books: Readarr will use the existing file name if false.
        :param pulumi.Input[bool] replace_illegal_characters: Replace illegal characters. They will be removed if false.
        :param pulumi.Input[str] standard_book_format: Standard book formatss.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Media Management -->Naming resource.
        For more information refer to [Naming](https://wiki.servarr.com/readarr/settings#community-naming-suggestions) documentation.

        ## Import

        import does not need parameters

        ```sh
         $ pulumi import readarr:MediaManagement/naming:Naming example ""
        ```

        :param str resource_name: The name of the resource.
        :param NamingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author_folder_format: Optional[pulumi.Input[str]] = None,
                 colon_replacement_format: Optional[pulumi.Input[int]] = None,
                 rename_books: Optional[pulumi.Input[bool]] = None,
                 replace_illegal_characters: Optional[pulumi.Input[bool]] = None,
                 standard_book_format: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamingArgs.__new__(NamingArgs)

            if author_folder_format is None and not opts.urn:
                raise TypeError("Missing required property 'author_folder_format'")
            __props__.__dict__["author_folder_format"] = author_folder_format
            if colon_replacement_format is None and not opts.urn:
                raise TypeError("Missing required property 'colon_replacement_format'")
            __props__.__dict__["colon_replacement_format"] = colon_replacement_format
            if rename_books is None and not opts.urn:
                raise TypeError("Missing required property 'rename_books'")
            __props__.__dict__["rename_books"] = rename_books
            if replace_illegal_characters is None and not opts.urn:
                raise TypeError("Missing required property 'replace_illegal_characters'")
            __props__.__dict__["replace_illegal_characters"] = replace_illegal_characters
            if standard_book_format is None and not opts.urn:
                raise TypeError("Missing required property 'standard_book_format'")
            __props__.__dict__["standard_book_format"] = standard_book_format
        super(Naming, __self__).__init__(
            'readarr:MediaManagement/naming:Naming',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            author_folder_format: Optional[pulumi.Input[str]] = None,
            colon_replacement_format: Optional[pulumi.Input[int]] = None,
            rename_books: Optional[pulumi.Input[bool]] = None,
            replace_illegal_characters: Optional[pulumi.Input[bool]] = None,
            standard_book_format: Optional[pulumi.Input[str]] = None) -> 'Naming':
        """
        Get an existing Naming resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] author_folder_format: Author folder format.
        :param pulumi.Input[int] colon_replacement_format: Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        :param pulumi.Input[bool] rename_books: Readarr will use the existing file name if false.
        :param pulumi.Input[bool] replace_illegal_characters: Replace illegal characters. They will be removed if false.
        :param pulumi.Input[str] standard_book_format: Standard book formatss.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamingState.__new__(_NamingState)

        __props__.__dict__["author_folder_format"] = author_folder_format
        __props__.__dict__["colon_replacement_format"] = colon_replacement_format
        __props__.__dict__["rename_books"] = rename_books
        __props__.__dict__["replace_illegal_characters"] = replace_illegal_characters
        __props__.__dict__["standard_book_format"] = standard_book_format
        return Naming(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorFolderFormat")
    def author_folder_format(self) -> pulumi.Output[str]:
        """
        Author folder format.
        """
        return pulumi.get(self, "author_folder_format")

    @property
    @pulumi.getter(name="colonReplacementFormat")
    def colon_replacement_format(self) -> pulumi.Output[int]:
        """
        Change how Readarr handles colon replacement. '0' Delete, '1' Dash, '2' Space Dash, '3' Space Dash Space, '4' Smart.
        """
        return pulumi.get(self, "colon_replacement_format")

    @property
    @pulumi.getter(name="renameBooks")
    def rename_books(self) -> pulumi.Output[bool]:
        """
        Readarr will use the existing file name if false.
        """
        return pulumi.get(self, "rename_books")

    @property
    @pulumi.getter(name="replaceIllegalCharacters")
    def replace_illegal_characters(self) -> pulumi.Output[bool]:
        """
        Replace illegal characters. They will be removed if false.
        """
        return pulumi.get(self, "replace_illegal_characters")

    @property
    @pulumi.getter(name="standardBookFormat")
    def standard_book_format(self) -> pulumi.Output[str]:
        """
        Standard book formatss.
        """
        return pulumi.get(self, "standard_book_format")

