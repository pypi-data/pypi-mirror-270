# coding: utf-8

# Standard Python imports
import io
from copy import deepcopy
from typing import Optional, Union, Tuple

# https://github.com/usnistgov/DataModelDict
from DataModelDict import DataModelDict as DM

# https://github.com/usnistgov/yabadaba
from yabadaba.record import Record
from yabadaba import load_query

# http://www.numpy.org/
import numpy as np
import numpy.typing as npt

class Dislocation(Record):
    """
    Class for representing dislocation records, which collect the parameters
    necessary for atomman to generate a particular dislocation type.
    """
    def __init__(self,
                 model: Union[str, io.IOBase, DM, None] = None,
                 name: Optional[str] = None,
                 database = None):
        """
        Initializes a Record object for a given style.
        
        Parameters
        ----------
        model : str, file-like object, DataModelDict
            The contents of the record.
        name : str, optional
            The unique name to assign to the record.  If model is a file
            path, then the default record name is the file name without
            extension.
        database : yabadaba.Database, optional
            Allows for a default database to be associated with the record.
        """
        super().__init__(model=model, name=name, database=database)

    @property
    def style(self) -> str:
        """str: The record style"""
        return 'dislocation'

    @property
    def xsd_filename(self) -> Tuple[str, str]:
        """tuple: The module path and file name of the record's xsd schema"""
        return ('atomman.library.xsd', f'{self.style}.xsd')

    @property
    def xsl_filename(self) -> Tuple[str, str]:
        """tuple: The module path and file name of the record's xsl transformer"""
        return ('atomman.library.xsl', f'{self.style}.xsl')

    @property
    def modelroot(self) -> str:
        """str: The root element of the content"""
        return 'dislocation'

    @property
    def key(self) -> str:
        """str : A UUID4 key assigned to the record"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__key

    @key.setter
    def key(self, value: str):
        self.__key = str(value)

    @property
    def id(self) -> str:
        """str : A unique id assigned to the record"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = str(value)

    @property
    def url(self) -> Optional[str]:
        """str : A URL where a copy of the record can be found"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__url

    @url.setter
    def url(self, value: Optional[str]):
        if value is None:
            self.__url = None
        else:
            self.__url = str(value)

    @property
    def character(self) -> str:
        """str : The dislocation's character"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__character

    @character.setter
    def character(self, value: str):
        self.__character = str(value)

    @property
    def burgers_vector(self) -> str:
        """str : String representation of the dislocation's Burgers vector"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__burgers_vector

    @burgers_vector.setter
    def burgers_vector(self, value: str):
        self.__burgers_vector = str(value)

    @property
    def slip_plane(self) -> np.ndarray:
        """numpy.NDArray : The dislocation's slip plane"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return deepcopy(self.__slip_plane)

    @slip_plane.setter
    def slip_plane(self, value: npt.ArrayLike):
        value = np.asarray(value, dtype=int)
        assert value.shape == (3,) or value.shape == (4,)
        self.__slip_plane = value

    @property
    def line_direction(self) -> np.ndarray:
        """numpy.NDArray : The dislocation's slip plane"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return deepcopy(self.__line_direction)

    @line_direction.setter
    def line_direction(self, value: npt.ArrayLike):
        value = np.asarray(value, dtype=int)
        assert value.shape == (3,) or value.shape == (4,)
        self.__line_direction = value

    @property
    def family(self) -> str:
        """str : The prototype/reference id the defect is defined for"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__family

    @family.setter
    def family(self, value: str):
        self.__family = str(value)

    @property
    def parameters(self) -> dict:
        """dict : Defect parameters for atomman structure generator"""
        if self.model is None:
            raise AttributeError('No model information loaded')
        return self.__parameters

    def load_model(self,
                   model: Union[str, io.IOBase, DM],
                   name: Optional[str] = None):
        """
        Loads record contents from a given model.

        Parameters
        ----------
        model : str or DataModelDict
            The model contents of the record to load.
        name : str, optional
            The name to assign to the record.  Often inferred from other
            attributes if not given.
        """
        super().load_model(model, name=name)
        content = self.model[self.modelroot]

        self.key = content['key']
        self.id = content['id']
        self.url = content.get('URL', None)
        self.character = content['character']
        self.burgers_vector = content['Burgers-vector']
        self.slip_plane = np.asarray(content['slip-plane'], dtype=int)
        self.line_direction = np.asarray(content['line-direction'], dtype=int)
        self.family = content['system-family']
        self.__parameters = dict(content['calculation-parameter'])

    def build_model(self) -> DM:
        """
        Returns the object info as data model content
        
        Returns
        ----------
        DataModelDict
            The data model content.
        """
        model = DM()
        model[self.modelroot] = content = DM()

        content['key'] = self.key
        content['id'] = self.id
        if self.url is not None:
            content['URL'] = self.url
        content['character'] = self.character
        content['Burgers-vector'] = self.burgers_vector
        content['slip-plane'] = self.slip_plane.tolist()
        content['line-direction'] = self.line_direction.tolist()
        content['system-family'] = self.family
        content['calculation-parameter'] = DM(self.parameters)

        self._set_model(model)
        return model

    def metadata(self) -> dict:
        """
        Generates a dict of simple metadata values associated with the record.
        Useful for quickly comparing records and for building pandas.DataFrames
        for multiple records of the same style.
        """
        meta = {}
        meta['name'] = self.name
        meta['key'] = self.key
        meta['id'] = self.id
        meta['url'] = self.url
        meta['character'] = self.character
        meta['burgers_vector'] = self.burgers_vector
        meta['slip_plane'] = self.slip_plane
        meta['line_direction'] = self.line_direction
        meta['family'] = self.family
        meta['slip_hkl'] = self.parameters['slip_hkl']
        meta['ξ_uvw'] = self.parameters['ξ_uvw']
        meta['burgers'] = self.parameters['burgers']
        meta['m'] = self.parameters['m']
        meta['n'] = self.parameters['n']
        if 'shift' in self.parameters:
            meta['shift'] = self.parameters['shift']
        if 'shiftscale' in self.parameters:
            meta['shiftscale'] = self.parameters['shiftscale']
        if 'shiftindex' in self.parameters:
            meta['shiftindex'] = self.parameters['shiftindex']

        return meta

    @property
    def queries(self) -> dict:
        """dict: Query objects and their associated parameter names."""
        return {
            'key': load_query(
                style='str_match',
                name='key',
                path=f'{self.modelroot}.key',
                description="search by dislocation parameter set's UUID key"),
            'id': load_query(
                style='str_match',
                name='id',
                path=f'{self.modelroot}.id',
                description="search by dislocation parameter set's id"),
            'character': load_query(
                style='str_match',
                name='character',
                path=f'{self.modelroot}.character',
                description="search by dislocation parameter set's dislocation character"),
            'family': load_query(
                style='str_match',
                name='family',
                path=f'{self.modelroot}.system-family',
                description="search by the crystal prototype that the dislocation parameter set is for"),
        }
