import os
import pytest
import time

from prelude_sdk.controllers.generate_controller import GenerateController
from prelude_sdk.controllers.iam_controller import IAMController

from testutils import *

@pytest.mark.order(9)
@pytest.mark.usefixtures('setup_account')
class TestGenerate:

    def setup_class(self):
        if not pytest.expected_account['features']['threat_intel']:
            pytest.skip("THREAT_INTEL feature not enabled")

        self.iam = IAMController(pytest.account)
        self.generate = GenerateController(pytest.account)

        self.threat_intel_pdf = os.path.dirname(os.path.realpath(__file__)) + '/data/threat_intel.pdf'

    def test_upload_threat_intel(self, unwrap):
        try:
            unwrap(self.iam.accept_terms)(self.iam, name='threat_intel', version='1.0.0')
        except Exception as e:
            pass

        res = unwrap(self.generate.upload_threat_intel)(self.generate, file=self.threat_intel_pdf)
        pytest.job_id = res['job_id']
        assert check_if_string_is_uuid(res['job_id'])

    def test_get_threat_intel(self, unwrap):
        while True:
            time.sleep(5)
            res = unwrap(self.generate.get_threat_intel)(self.generate, job_id=pytest.job_id)
            match status := res.get('status'):
                case 'RUNNING':
                    if res['step'] == 'GENERATE':
                        assert 9 == res['num_tasks'], json.dumps(res)
                case 'COMPLETE':
                    assert 9 == len(res['output']), json.dumps(res)
                    assert {'go_code', 'name', 'sigma_rules', 'status', 'technique'} == set(res['output'][0].keys()), json.dumps(res)
                    return
                case 'FAILED':
                    assert False, f'threat_gen FAILED: {json.dumps(res)}'
                case _:
                    assert False, f' Unexpected status: {status}\n Response: {json.dumps(res)}'
                