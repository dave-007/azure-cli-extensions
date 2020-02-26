# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6237, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class IntegrationRuntimeType(str, Enum):

    managed = "Managed"
    self_hosted = "SelfHosted"

class SsisObjectMetadataType(str, Enum):

    folder = "Folder"
    project = "Project"
    package = "Package"
    environment = "Environment"

class ParameterType(str, Enum):

    object_enum = "Object"
    string = "String"
    int_enum = "Int"
    float_enum = "Float"
    bool_enum = "Bool"
    array = "Array"
    secure_string = "SecureString"

class DependencyCondition(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    skipped = "Skipped"
    completed = "Completed"

class VariableType(str, Enum):

    string = "String"
    bool_enum = "Bool"
    array = "Array"

class RunQueryFilterOperand(str, Enum):

    pipeline_name = "PipelineName"
    status = "Status"
    run_start = "RunStart"
    run_end = "RunEnd"
    activity_name = "ActivityName"
    activity_run_start = "ActivityRunStart"
    activity_run_end = "ActivityRunEnd"
    activity_type = "ActivityType"
    trigger_name = "TriggerName"
    trigger_run_timestamp = "TriggerRunTimestamp"
    run_group_id = "RunGroupId"
    latest_only = "LatestOnly"

class RunQueryFilterOperator(str, Enum):

    equals = "Equals"
    not_equals = "NotEquals"
    in_enum = "In"
    not_in = "NotIn"

class RunQueryOrderByField(str, Enum):

    run_start = "RunStart"
    run_end = "RunEnd"
    pipeline_name = "PipelineName"
    status = "Status"
    activity_name = "ActivityName"
    activity_run_start = "ActivityRunStart"
    activity_run_end = "ActivityRunEnd"
    trigger_name = "TriggerName"
    trigger_run_timestamp = "TriggerRunTimestamp"

class RunQueryOrder(str, Enum):

    asc = "ASC"
    desc = "DESC"

class TriggerRuntimeState(str, Enum):

    started = "Started"
    stopped = "Stopped"
    disabled = "Disabled"

class TriggerRunStatus(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    inprogress = "Inprogress"

class IntegrationRuntimeState(str, Enum):

    initial = "Initial"
    stopped = "Stopped"
    started = "Started"
    starting = "Starting"
    stopping = "Stopping"
    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    access_denied = "AccessDenied"

class ManagedIntegrationRuntimeNodeStatus(str, Enum):

    starting = "Starting"
    available = "Available"
    recycling = "Recycling"
    unavailable = "Unavailable"

class SelfHostedIntegrationRuntimeNodeStatus(str, Enum):

    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    upgrading = "Upgrading"
    initializing = "Initializing"
    initialize_failed = "InitializeFailed"

class IntegrationRuntimeUpdateResult(str, Enum):

    none = "None"
    succeed = "Succeed"
    fail = "Fail"

class DaysOfWeek(str, Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"

class DayOfWeek(str, Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"

class BlobEventTypes(str, Enum):

    microsoft_storage_blob_created = "Microsoft.Storage.BlobCreated"
    microsoft_storage_blob_deleted = "Microsoft.Storage.BlobDeleted"

class HdiNodeTypes(str, Enum):

    headnode = "Headnode"
    workernode = "Workernode"
    zookeeper = "Zookeeper"

class IntegrationRuntimeAutoUpdate(str, Enum):

    on = "On"
    off = "Off"

class IntegrationRuntimeAuthKeyName(str, Enum):

    auth_key1 = "authKey1"
    auth_key2 = "authKey2"

class EventSubscriptionStatus(str, Enum):

    enabled = "Enabled"
    provisioning = "Provisioning"
    deprovisioning = "Deprovisioning"
    disabled = "Disabled"
    unknown = "Unknown"

class DataFlowDebugCommandType(str, Enum):

    execute_preview_query = "executePreviewQuery"
    execute_statistics_query = "executeStatisticsQuery"
    execute_expression_query = "executeExpressionQuery"

class DataFlowComputeType(str, Enum):

    general = "General"
    memory_optimized = "MemoryOptimized"
    compute_optimized = "ComputeOptimized"

class IntegrationRuntimeSsisCatalogPricingTier(str, Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"

class IntegrationRuntimeLicenseType(str, Enum):

    base_price = "BasePrice"
    license_included = "LicenseIncluded"

class IntegrationRuntimeEntityReferenceType(str, Enum):

    integration_runtime_reference = "IntegrationRuntimeReference"
    linked_service_reference = "LinkedServiceReference"

class IntegrationRuntimeEdition(str, Enum):

    standard = "Standard"
    enterprise = "Enterprise"

class IntegrationRuntimeInternalChannelEncryptionMode(str, Enum):

    not_set = "NotSet"
    ssl_encrypted = "SslEncrypted"
    not_encrypted = "NotEncrypted"

class JsonWriteFilePattern(str, Enum):

    set_of_objects = "setOfObjects"
    array_of_objects = "arrayOfObjects"

class SalesforceSourceReadBehavior(str, Enum):

    query = "Query"
    query_all = "QueryAll"

class SapHanaPartitionOption(str, Enum):

    none = "None"
    physical_partitions_of_table = "PhysicalPartitionsOfTable"
    sap_hana_dynamic_range = "SapHanaDynamicRange"

class SapTablePartitionOption(str, Enum):

    none = "None"
    partition_on_int = "PartitionOnInt"
    partition_on_calendar_year = "PartitionOnCalendarYear"
    partition_on_calendar_month = "PartitionOnCalendarMonth"
    partition_on_calendar_date = "PartitionOnCalendarDate"
    partition_on_time = "PartitionOnTime"

class StoredProcedureParameterType(str, Enum):

    string = "String"
    int_enum = "Int"
    int64 = "Int64"
    decimal_enum = "Decimal"
    guid = "Guid"
    boolean = "Boolean"
    date_enum = "Date"

class OraclePartitionOption(str, Enum):

    none = "None"
    physical_partitions_of_table = "PhysicalPartitionsOfTable"
    dynamic_range = "DynamicRange"

class TeradataPartitionOption(str, Enum):

    none = "None"
    hash = "Hash"
    dynamic_range = "DynamicRange"

class CassandraSourceReadConsistencyLevels(str, Enum):

    all = "ALL"
    each_quorum = "EACH_QUORUM"
    quorum = "QUORUM"
    local_quorum = "LOCAL_QUORUM"
    one = "ONE"
    two = "TWO"
    three = "THREE"
    local_one = "LOCAL_ONE"
    serial = "SERIAL"
    local_serial = "LOCAL_SERIAL"

class NetezzaPartitionOption(str, Enum):

    none = "None"
    data_slice = "DataSlice"
    dynamic_range = "DynamicRange"

class SapCloudForCustomerSinkWriteBehavior(str, Enum):

    insert = "Insert"
    update = "Update"

class PolybaseSettingsRejectType(str, Enum):

    value = "value"
    percentage = "percentage"

class AzureSearchIndexWriteBehaviorType(str, Enum):

    merge = "Merge"
    upload = "Upload"

class SalesforceSinkWriteBehavior(str, Enum):

    insert = "Insert"
    upsert = "Upsert"

class HDInsightActivityDebugInfoOption(str, Enum):

    none = "None"
    always = "Always"
    failure = "Failure"

class SsisPackageLocationType(str, Enum):

    ssisdb = "SSISDB"
    file = "File"
    inline_package = "InlinePackage"

class WebActivityMethod(str, Enum):

    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"

class AzureFunctionActivityMethod(str, Enum):

    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    options = "OPTIONS"
    head = "HEAD"
    trace = "TRACE"

class RecurrenceFrequency(str, Enum):

    not_specified = "NotSpecified"
    minute = "Minute"
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"
    year = "Year"

class TumblingWindowFrequency(str, Enum):

    minute = "Minute"
    hour = "Hour"

class JsonFormatFilePattern(str, Enum):

    set_of_objects = "setOfObjects"
    array_of_objects = "arrayOfObjects"

class DatasetCompressionLevel(str, Enum):

    optimal = "Optimal"
    fastest = "Fastest"

class AvroCompressionCodec(str, Enum):

    none = "none"
    deflate = "deflate"
    snappy = "snappy"
    xz = "xz"
    bzip2 = "bzip2"

class CompressionCodec(str, Enum):

    none = "none"
    gzip = "gzip"
    snappy = "snappy"
    lzo = "lzo"
    bzip2 = "bzip2"
    deflate = "deflate"
    zip_deflate = "zipDeflate"
    lz4 = "lz4"

class OrcCompressionCodec(str, Enum):

    none = "none"
    zlib = "zlib"
    snappy = "snappy"

class DynamicsDeploymentType(str, Enum):

    online = "Online"
    on_premises_with_ifd = "OnPremisesWithIfd"

class DynamicsAuthenticationType(str, Enum):

    office365 = "Office365"
    ifd = "Ifd"
    aad_service_principal = "AADServicePrincipal"

class DynamicsServicePrincipalCredentialType(str, Enum):

    service_principal_key = "ServicePrincipalKey"
    service_principal_cert = "ServicePrincipalCert"

class SybaseAuthenticationType(str, Enum):

    basic = "Basic"
    windows = "Windows"

class TeradataAuthenticationType(str, Enum):

    basic = "Basic"
    windows = "Windows"

class ODataAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"
    windows = "Windows"
    aad_service_principal = "AadServicePrincipal"
    managed_service_identity = "ManagedServiceIdentity"

class ODataAadServicePrincipalCredentialType(str, Enum):

    service_principal_key = "ServicePrincipalKey"
    service_principal_cert = "ServicePrincipalCert"

class WebAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"
    client_certificate = "ClientCertificate"

class MongoDbAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"

class RestServiceAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    basic = "Basic"
    aad_service_principal = "AadServicePrincipal"
    managed_service_identity = "ManagedServiceIdentity"

class HttpAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"
    digest = "Digest"
    windows = "Windows"
    client_certificate = "ClientCertificate"

class FtpAuthenticationType(str, Enum):

    basic = "Basic"
    anonymous = "Anonymous"

class SftpAuthenticationType(str, Enum):

    basic = "Basic"
    ssh_public_key = "SshPublicKey"

class SapHanaAuthenticationType(str, Enum):

    basic = "Basic"
    windows = "Windows"

class GoogleBigQueryAuthenticationType(str, Enum):

    service_authentication = "ServiceAuthentication"
    user_authentication = "UserAuthentication"

class HBaseAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    basic = "Basic"

class HiveServerType(str, Enum):

    hive_server1 = "HiveServer1"
    hive_server2 = "HiveServer2"
    hive_thrift_server = "HiveThriftServer"

class HiveThriftTransportProtocol(str, Enum):

    binary = "Binary"
    sasl = "SASL"
    http = "HTTP "

class HiveAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    username = "Username"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"

class ImpalaAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    sasl_username = "SASLUsername"
    username_and_password = "UsernameAndPassword"

class PhoenixAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"

class PrestoAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    ldap = "LDAP"

class ServiceNowAuthenticationType(str, Enum):

    basic = "Basic"
    oauth2 = "OAuth2"

class SparkServerType(str, Enum):

    shark_server = "SharkServer"
    shark_server2 = "SharkServer2"
    spark_thrift_server = "SparkThriftServer"

class SparkThriftTransportProtocol(str, Enum):

    binary = "Binary"
    sasl = "SASL"
    http = "HTTP "

class SparkAuthenticationType(str, Enum):

    anonymous = "Anonymous"
    username = "Username"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"

class GoogleAdWordsAuthenticationType(str, Enum):

    service_authentication = "ServiceAuthentication"
    user_authentication = "UserAuthentication"
