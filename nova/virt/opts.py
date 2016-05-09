# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools

import nova.virt.libvirt.volume.remotefs
import nova.virt.libvirt.volume.scality
import nova.virt.libvirt.volume.smbfs
import nova.virt.xenapi.agent
import nova.virt.xenapi.pool
import nova.virt.xenapi.vif
import nova.virt.xenapi.vmops
import nova.virt.xenapi.volume_utils


def list_opts():
    return [
        ('libvirt',
         itertools.chain(
             nova.virt.libvirt.volume.remotefs.libvirt_opts,
             nova.virt.libvirt.volume.scality.volume_opts,
             nova.virt.libvirt.volume.smbfs.volume_opts,
         )),
        ('xenserver',
         itertools.chain(
             [nova.virt.xenapi.vif.xenapi_ovs_integration_bridge_opt],
             nova.virt.xenapi.pool.xenapi_pool_opts,
             nova.virt.xenapi.volume_utils.xenapi_volume_utils_opts,
         )),
    ]
