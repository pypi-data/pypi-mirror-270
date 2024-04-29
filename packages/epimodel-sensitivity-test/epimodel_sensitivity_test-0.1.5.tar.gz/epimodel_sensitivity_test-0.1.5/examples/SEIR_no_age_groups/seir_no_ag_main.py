from types import SimpleNamespace

import torch

from examples.SEIR_no_age_groups.simulation_seir import SimulationSEIR


def main():
    params = {"gamma": 0.2, "beta": 0.2, "alpha": 0.3}
    contact_data = torch.tensor([[1]])
    age_data = torch.tensor([[10000]])
    data = SimpleNamespace(**{"params": params,
                              "cm": contact_data,
                              "age_data": age_data,
                              "n_age": 1,
                              "device": "cpu"})

    sim = SimulationSEIR(data)
    sim.run_sampling()
    sim.calculate_all_prcc()
    sim.calculate_all_p_values()
    sim.plot_all_prcc()


if __name__ == "__main__":
    main()
