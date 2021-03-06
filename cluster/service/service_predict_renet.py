from cluster.service.service_predict import PredictNet
from cluster.neuralnet.neuralnet_node_image import NeuralNetNodeImage

class PredictNetRenet(PredictNet):
    def run(self, nn_id, ver, parm):
        """
        run predict service
        1. get node id
        2. check json conf format
        3. run predict & return
        :param parm:
        :return:
        """
        if(self._valid_check(parm)) :
            if (ver == 'active'):
                return NeuralNetNodeImage().predict(self._find_netconf_node_id(nn_id), parm)
            else:
                return NeuralNetNodeImage().predict(self._find_netconf_node_id(nn_id, ver), parm)

    def _valid_check(self, parm):
        return True