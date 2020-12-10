# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AccountKeyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of account key to regenerate.
    """

    PRIMARY = "Primary"  #: The primary account key.
    SECONDARY = "Secondary"  #: The secondary account key.

class AllocationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether the pool is resizing.
    """

    STEADY = "Steady"  #: The pool is not resizing. There are no changes to the number of nodes in the pool in progress. A pool enters this state when it is created and when no operations are being performed on the pool to change the number of nodes.
    RESIZING = "Resizing"  #: The pool is resizing; that is, compute nodes are being added to or removed from the pool.
    STOPPING = "Stopping"  #: The pool was resizing, but the user has requested that the resize be stopped, but the stop request has not yet been completed.

class AutoUserScope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default value is Pool. If the pool is running Windows a value of Task should be specified
    if stricter isolation between tasks is required. For example, if the task mutates the registry
    in a way which could impact other tasks, or if certificates have been specified on the pool
    which should not be accessible by normal tasks but should be accessible by start tasks.
    """

    TASK = "Task"  #: Specifies that the service should create a new user for the task.
    POOL = "Pool"  #: Specifies that the task runs as the common auto user account which is created on every node in a pool.

class CachingType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of caching to enable for the disk.
    """

    NONE = "None"  #: The caching mode for the disk is not enabled.
    READ_ONLY = "ReadOnly"  #: The caching mode for the disk is read only.
    READ_WRITE = "ReadWrite"  #: The caching mode for the disk is read and write.

class CertificateFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.
    """

    PFX = "Pfx"  #: The certificate is a PFX (PKCS#12) formatted certificate or certificate chain.
    CER = "Cer"  #: The certificate is a base64-encoded X.509 certificate.

class CertificateProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCEEDED = "Succeeded"  #: The certificate is available for use in pools.
    DELETING = "Deleting"  #: The user has requested that the certificate be deleted, but the delete operation has not yet completed. You may not reference the certificate when creating or updating pools.
    FAILED = "Failed"  #: The user requested that the certificate be deleted, but there are pools that still have references to the certificate, or it is still installed on one or more compute nodes. (The latter can occur if the certificate has been removed from the pool, but the node has not yet restarted. Nodes refresh their certificates only when they restart.) You may use the cancel certificate delete operation to cancel the delete, or the delete certificate operation to retry the delete.

class CertificateStoreLocation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default value is currentUser. This property is applicable only for pools configured with
    Windows nodes (that is, created with cloudServiceConfiguration, or with
    virtualMachineConfiguration using a Windows image reference). For Linux compute nodes, the
    certificates are stored in a directory inside the task working directory and an environment
    variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For
    certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home
    directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory.
    """

    CURRENT_USER = "CurrentUser"  #: Certificates should be installed to the CurrentUser certificate store.
    LOCAL_MACHINE = "LocalMachine"  #: Certificates should be installed to the LocalMachine certificate store.

class CertificateVisibility(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    START_TASK = "StartTask"  #: The certificate should be visible to the user account under which the start task is run. Note that if AutoUser Scope is Pool for both the StartTask and a Task, this certificate will be visible to the Task as well.
    TASK = "Task"  #: The certificate should be visible to the user accounts under which job tasks are run.
    REMOTE_USER = "RemoteUser"  #: The certificate should be visible to the user accounts under which users remotely access the node.

class ComputeNodeDeallocationOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Determines what to do with a node and its running task(s) after it has been selected for
    deallocation.
    """

    REQUEUE = "Requeue"  #: Terminate running task processes and requeue the tasks. The tasks will run again when a node is available. Remove nodes as soon as tasks have been terminated.
    TERMINATE = "Terminate"  #: Terminate running tasks. The tasks will be completed with failureInfo indicating that they were terminated, and will not run again. Remove nodes as soon as tasks have been terminated.
    TASK_COMPLETION = "TaskCompletion"  #: Allow currently running tasks to complete. Schedule no new tasks while waiting. Remove nodes when all tasks have completed.
    RETAINED_DATA = "RetainedData"  #: Allow currently running tasks to complete, then wait for all task data retention periods to expire. Schedule no new tasks while waiting. Remove nodes when all task retention periods have expired.

class ComputeNodeFillType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """How tasks should be distributed across compute nodes.
    """

    SPREAD = "Spread"  #: Tasks should be assigned evenly across all nodes in the pool.
    PACK = "Pack"  #: As many tasks as possible (taskSlotsPerNode) should be assigned to each node in the pool before any tasks are assigned to the next node in the pool.

class ContainerWorkingDirectory(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A flag to indicate where the container task working directory is. The default is
    'taskWorkingDirectory'.
    """

    TASK_WORKING_DIRECTORY = "TaskWorkingDirectory"  #: Use the standard Batch service task working directory, which will contain the Task resource files populated by Batch.
    CONTAINER_IMAGE_DEFAULT = "ContainerImageDefault"  #: Using container image defined working directory. Beware that this directory will not contain the resource files downloaded by Batch.

class DiskEncryptionTarget(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """If omitted, no disks on the compute nodes in the pool will be encrypted.
    """

    OS_DISK = "OsDisk"  #: The OS Disk on the compute node is encrypted.
    TEMPORARY_DISK = "TemporaryDisk"  #: The temporary disk on the compute node is encrypted. On Linux this encryption applies to other partitions (such as those on mounted data disks) when encryption occurs at boot time.

class ElevationLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The elevation level of the user.
    """

    NON_ADMIN = "NonAdmin"  #: The user is a standard user without elevated access.
    ADMIN = "Admin"  #: The user is a user with elevated access and operates with full Administrator permissions.

class InboundEndpointProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol of the endpoint.
    """

    TCP = "TCP"  #: Use TCP for the endpoint.
    UDP = "UDP"  #: Use UDP for the endpoint.

class InterNodeCommunicationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can
    reduce the chance of the requested number of nodes to be allocated in the pool. If not
    specified, this value defaults to 'Disabled'.
    """

    ENABLED = "Enabled"  #: Enable network communication between virtual machines.
    DISABLED = "Disabled"  #: Disable network communication between virtual machines.

class IPAddressProvisioningType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning type for Public IP Addresses for the Batch Pool.
    """

    BATCH_MANAGED = "BatchManaged"  #: A public IP will be created and managed by Batch. There may be multiple public IPs depending on the size of the Pool.
    USER_MANAGED = "UserManaged"  #: Public IPs are provided by the user and will be used to provision the Compute Nodes.
    NO_PUBLIC_IP_ADDRESSES = "NoPublicIPAddresses"  #: No public IP Address will be created for the Compute Nodes in the Pool.

class KeySource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the key source.
    """

    MICROSOFT_BATCH = "Microsoft.Batch"  #: Batch creates and manages the encryption keys used to protect the account data.
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"  #: The encryption keys used to protect the account data are stored in an external key vault. If this is set then the Batch Account identity must be set to ``SystemAssigned`` and a valid Key Identifier must also be supplied under the keyVaultProperties.

class LoginMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies login mode for the user. The default value for VirtualMachineConfiguration pools is
    interactive mode and for CloudServiceConfiguration pools is batch mode.
    """

    BATCH = "Batch"  #: The LOGON32_LOGON_BATCH Win32 login mode. The batch login mode is recommended for long running parallel processes.
    INTERACTIVE = "Interactive"  #: The LOGON32_LOGON_INTERACTIVE Win32 login mode. Some applications require having permissions associated with the interactive login mode. If this is the case for an application used in your task, then this option is recommended.

class NameAvailabilityReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the reason that a Batch account name could not be used. The Reason element is only
    returned if NameAvailable is false.
    """

    INVALID = "Invalid"  #: The requested name is invalid.
    ALREADY_EXISTS = "AlreadyExists"  #: The requested name is already in use.

class NetworkSecurityGroupRuleAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The action that should be taken for a specified IP address, subnet range or tag.
    """

    ALLOW = "Allow"  #: Allow access.
    DENY = "Deny"  #: Deny access.

class PackageState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the application package.
    """

    PENDING = "Pending"  #: The application package has been created but has not yet been activated.
    ACTIVE = "Active"  #: The application package is ready for use.

class PoolAllocationMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The allocation mode for creating pools in the Batch account.
    """

    BATCH_SERVICE = "BatchService"  #: Pools will be allocated in subscriptions owned by the Batch service.
    USER_SUBSCRIPTION = "UserSubscription"  #: Pools will be allocated in a subscription owned by the user.

class PoolProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the pool.
    """

    SUCCEEDED = "Succeeded"  #: The pool is available to run tasks subject to the availability of compute nodes.
    DELETING = "Deleting"  #: The user has requested that the pool be deleted, but the delete operation has not yet completed.

class PrivateEndpointConnectionProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the private endpoint connection.
    """

    SUCCEEDED = "Succeeded"  #: The connection status is final and is ready for use if Status is Approved.
    UPDATING = "Updating"  #: The user has requested that the connection status be updated, but the update operation has not yet completed. You may not reference the connection when connecting the Batch account.
    FAILED = "Failed"  #: The user requested that the connection be updated and it failed. You may retry the update operation.

class PrivateLinkServiceConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the Batch private endpoint connection
    """

    APPROVED = "Approved"  #: The private endpoint connection is approved and can be used to access Batch account.
    PENDING = "Pending"  #: The private endpoint connection is pending and cannot be used to access Batch account.
    REJECTED = "Rejected"  #: The private endpoint connection is rejected and cannot be used to access Batch account.
    DISCONNECTED = "Disconnected"  #: The private endpoint connection is disconnected and cannot be used to access Batch account.

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioned state of the resource
    """

    INVALID = "Invalid"  #: The account is in an invalid state.
    CREATING = "Creating"  #: The account is being created.
    DELETING = "Deleting"  #: The account is being deleted.
    SUCCEEDED = "Succeeded"  #: The account has been created and is ready for use.
    FAILED = "Failed"  #: The last operation for the account is failed.
    CANCELLED = "Cancelled"  #: The last operation for the account is cancelled.

class PublicNetworkAccessType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The network access type for operating on the resources in the Batch account.
    """

    ENABLED = "Enabled"  #: Enables connectivity to Azure Batch through public DNS.
    DISABLED = "Disabled"  #: Disables public connectivity and enables private connectivity to Azure Batch Service through private endpoint resource.

class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for the Batch account.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"  #: Batch account has a system assigned identity with it.
    NONE = "None"  #: Batch account has no identity associated with it. Setting ``None`` in update account will remove existing identities.

class StorageAccountType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The storage account type for use in creating data disks.
    """

    STANDARD_LRS = "Standard_LRS"  #: The data disk should use standard locally redundant storage.
    PREMIUM_LRS = "Premium_LRS"  #: The data disk should use premium locally redundant storage.