# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AuthorArgs', 'Author']

@pulumi.input_type
class AuthorArgs:
    def __init__(__self__, *,
                 author_name: pulumi.Input[str],
                 foreign_author_id: pulumi.Input[str],
                 monitored: pulumi.Input[bool],
                 path: pulumi.Input[str],
                 quality_profile_id: pulumi.Input[int],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Author resource.
        :param pulumi.Input[str] author_name: Author name.
        :param pulumi.Input[str] foreign_author_id: Foreign author ID.
        :param pulumi.Input[bool] monitored: Monitored flag.
        :param pulumi.Input[str] path: Full author path.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "author_name", author_name)
        pulumi.set(__self__, "foreign_author_id", foreign_author_id)
        pulumi.set(__self__, "monitored", monitored)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authorName")
    def author_name(self) -> pulumi.Input[str]:
        """
        Author name.
        """
        return pulumi.get(self, "author_name")

    @author_name.setter
    def author_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "author_name", value)

    @property
    @pulumi.getter(name="foreignAuthorId")
    def foreign_author_id(self) -> pulumi.Input[str]:
        """
        Foreign author ID.
        """
        return pulumi.get(self, "foreign_author_id")

    @foreign_author_id.setter
    def foreign_author_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "foreign_author_id", value)

    @property
    @pulumi.getter
    def monitored(self) -> pulumi.Input[bool]:
        """
        Monitored flag.
        """
        return pulumi.get(self, "monitored")

    @monitored.setter
    def monitored(self, value: pulumi.Input[bool]):
        pulumi.set(self, "monitored", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        Full author path.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> pulumi.Input[int]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @quality_profile_id.setter
    def quality_profile_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "quality_profile_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AuthorState:
    def __init__(__self__, *,
                 author_name: Optional[pulumi.Input[str]] = None,
                 foreign_author_id: Optional[pulumi.Input[str]] = None,
                 genres: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 monitored: Optional[pulumi.Input[bool]] = None,
                 overview: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Author resources.
        :param pulumi.Input[str] author_name: Author name.
        :param pulumi.Input[str] foreign_author_id: Foreign author ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] genres: List genres.
        :param pulumi.Input[bool] monitored: Monitored flag.
        :param pulumi.Input[str] overview: Overview.
        :param pulumi.Input[str] path: Full author path.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] status: Author status.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if author_name is not None:
            pulumi.set(__self__, "author_name", author_name)
        if foreign_author_id is not None:
            pulumi.set(__self__, "foreign_author_id", foreign_author_id)
        if genres is not None:
            pulumi.set(__self__, "genres", genres)
        if monitored is not None:
            pulumi.set(__self__, "monitored", monitored)
        if overview is not None:
            pulumi.set(__self__, "overview", overview)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if quality_profile_id is not None:
            pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authorName")
    def author_name(self) -> Optional[pulumi.Input[str]]:
        """
        Author name.
        """
        return pulumi.get(self, "author_name")

    @author_name.setter
    def author_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "author_name", value)

    @property
    @pulumi.getter(name="foreignAuthorId")
    def foreign_author_id(self) -> Optional[pulumi.Input[str]]:
        """
        Foreign author ID.
        """
        return pulumi.get(self, "foreign_author_id")

    @foreign_author_id.setter
    def foreign_author_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "foreign_author_id", value)

    @property
    @pulumi.getter
    def genres(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List genres.
        """
        return pulumi.get(self, "genres")

    @genres.setter
    def genres(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "genres", value)

    @property
    @pulumi.getter
    def monitored(self) -> Optional[pulumi.Input[bool]]:
        """
        Monitored flag.
        """
        return pulumi.get(self, "monitored")

    @monitored.setter
    def monitored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "monitored", value)

    @property
    @pulumi.getter
    def overview(self) -> Optional[pulumi.Input[str]]:
        """
        Overview.
        """
        return pulumi.get(self, "overview")

    @overview.setter
    def overview(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "overview", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Full author path.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> Optional[pulumi.Input[int]]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @quality_profile_id.setter
    def quality_profile_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "quality_profile_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Author status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tags", value)


class Author(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author_name: Optional[pulumi.Input[str]] = None,
                 foreign_author_id: Optional[pulumi.Input[str]] = None,
                 monitored: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Authors -->Author resource.
        For more information refer to [Authors](https://wiki.servarr.com/readarr/library#authors) documentation.

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import readarr:Authors/author:Author example 10
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] author_name: Author name.
        :param pulumi.Input[str] foreign_author_id: Foreign author ID.
        :param pulumi.Input[bool] monitored: Monitored flag.
        :param pulumi.Input[str] path: Full author path.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Authors -->Author resource.
        For more information refer to [Authors](https://wiki.servarr.com/readarr/library#authors) documentation.

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import readarr:Authors/author:Author example 10
        ```

        :param str resource_name: The name of the resource.
        :param AuthorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author_name: Optional[pulumi.Input[str]] = None,
                 foreign_author_id: Optional[pulumi.Input[str]] = None,
                 monitored: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorArgs.__new__(AuthorArgs)

            if author_name is None and not opts.urn:
                raise TypeError("Missing required property 'author_name'")
            __props__.__dict__["author_name"] = author_name
            if foreign_author_id is None and not opts.urn:
                raise TypeError("Missing required property 'foreign_author_id'")
            __props__.__dict__["foreign_author_id"] = foreign_author_id
            if monitored is None and not opts.urn:
                raise TypeError("Missing required property 'monitored'")
            __props__.__dict__["monitored"] = monitored
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            if quality_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'quality_profile_id'")
            __props__.__dict__["quality_profile_id"] = quality_profile_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["genres"] = None
            __props__.__dict__["overview"] = None
            __props__.__dict__["status"] = None
        super(Author, __self__).__init__(
            'readarr:Authors/author:Author',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            author_name: Optional[pulumi.Input[str]] = None,
            foreign_author_id: Optional[pulumi.Input[str]] = None,
            genres: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            monitored: Optional[pulumi.Input[bool]] = None,
            overview: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            quality_profile_id: Optional[pulumi.Input[int]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Author':
        """
        Get an existing Author resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] author_name: Author name.
        :param pulumi.Input[str] foreign_author_id: Foreign author ID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] genres: List genres.
        :param pulumi.Input[bool] monitored: Monitored flag.
        :param pulumi.Input[str] overview: Overview.
        :param pulumi.Input[str] path: Full author path.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] status: Author status.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuthorState.__new__(_AuthorState)

        __props__.__dict__["author_name"] = author_name
        __props__.__dict__["foreign_author_id"] = foreign_author_id
        __props__.__dict__["genres"] = genres
        __props__.__dict__["monitored"] = monitored
        __props__.__dict__["overview"] = overview
        __props__.__dict__["path"] = path
        __props__.__dict__["quality_profile_id"] = quality_profile_id
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        return Author(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorName")
    def author_name(self) -> pulumi.Output[str]:
        """
        Author name.
        """
        return pulumi.get(self, "author_name")

    @property
    @pulumi.getter(name="foreignAuthorId")
    def foreign_author_id(self) -> pulumi.Output[str]:
        """
        Foreign author ID.
        """
        return pulumi.get(self, "foreign_author_id")

    @property
    @pulumi.getter
    def genres(self) -> pulumi.Output[Sequence[str]]:
        """
        List genres.
        """
        return pulumi.get(self, "genres")

    @property
    @pulumi.getter
    def monitored(self) -> pulumi.Output[bool]:
        """
        Monitored flag.
        """
        return pulumi.get(self, "monitored")

    @property
    @pulumi.getter
    def overview(self) -> pulumi.Output[str]:
        """
        Overview.
        """
        return pulumi.get(self, "overview")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Full author path.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> pulumi.Output[int]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Author status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

