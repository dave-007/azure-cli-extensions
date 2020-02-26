# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6237, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ExposureControlOperations(object):
    """ExposureControlOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_factory_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_feature_value(
        self,
        location_id,  # type: str
        feature_name=None,  # type: Optional[str]
        feature_type=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ExposureControlResponse"
        """Get exposure control feature for specific location.

        :param location_id: The location identifier.
        :type location_id: str
        :param feature_name: The feature name.
        :type feature_name: str
        :param feature_type: The feature type.
        :type feature_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~data_factory_management_client.models.ExposureControlResponse
        :raises: ~data_factory_management_client.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ExposureControlResponse"]
        error_map = kwargs.pop('error_map', {})

        exposure_control_request = models.ExposureControlRequest(feature_name=feature_name, feature_type=feature_type)
        api_version = "2018-06-01"

        # Construct URL
        url = self.get_feature_value.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'locationId': self._serialize.url("location_id", location_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(exposure_control_request, 'ExposureControlRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ExposureControlResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_feature_value.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue'}

    def get_feature_value_by_factory(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        feature_name=None,  # type: Optional[str]
        feature_type=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ExposureControlResponse"
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param feature_name: The feature name.
        :type feature_name: str
        :param feature_type: The feature type.
        :type feature_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~data_factory_management_client.models.ExposureControlResponse
        :raises: ~data_factory_management_client.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ExposureControlResponse"]
        error_map = kwargs.pop('error_map', {})

        exposure_control_request = models.ExposureControlRequest(feature_name=feature_name, feature_type=feature_type)
        api_version = "2018-06-01"

        # Construct URL
        url = self.get_feature_value_by_factory.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern='^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(exposure_control_request, 'ExposureControlRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ExposureControlResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_feature_value_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue'}
