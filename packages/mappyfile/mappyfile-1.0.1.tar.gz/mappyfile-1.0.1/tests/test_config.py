import logging
import json
import pytest
from mappyfile.parser import Parser
from mappyfile.pprint import PrettyPrinter
from mappyfile.transformer import MapfileToDict
from mappyfile.validator import Validator


def output(s, include_position=True, schema_name="map"):
    """
    Parse, transform, validate, and pretty print
    the result
    """
    p = Parser(is_config=True)
    m = MapfileToDict(include_position=include_position)
    ast = p.parse(s)
    logging.debug(ast.pretty())
    d = m.transform(ast)
    logging.debug(json.dumps(d, indent=4))
    v = Validator()
    errors = v.validate(d, schema_name=schema_name)
    logging.error(errors)
    assert len(errors) == 0
    pp = PrettyPrinter(indent=0, newlinechar=" ", quote="'")
    # pp = PrettyPrinter()
    s = pp.pprint(d)
    logging.debug(s)
    return s


def test_config_file():
    s = r"""
    CONFIG
      ENV
        "ms_map_pattern" "."
      END
      MAPS
        "itasca" "C:/MapServer/apps/itasca.map"
      END
      PLUGINS
        "mssql" "C:/MapServer/bin/ms/plugins/mssql2008/msplugin_mssql2008.dll"
      END
    END
    """

    print(output(s, schema_name="config"))
    exp = (
        "CONFIG "
        "ENV \"MS_MAP_PATTERN\" '.' END "
        "MAPS \"ITASCA\" 'C:/MapServer/apps/itasca.map' END "
        "PLUGINS \"MSSQL\" 'C:/MapServer/bin/ms/plugins/mssql2008/msplugin_mssql2008.dll' END "
        "END"
    )
    # exp = "CONFIG ENV MS_MAP_PATTERN '.' END MAPS ITASCA 'C:/MapServer/apps/itasca.map' END PLUGINS ""MSSQL"" 'C:/MapServer/bin/ms/plugins/mssql2008/msplugin_mssql2008.dll' END END"    
    assert output(s, schema_name="config") == exp


def run_tests():
    pytest.main(["tests/test_config.py"])


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run_tests()
    print("Done!")
