class FMEFeature:
    """FME Feature Class"""

    def __init__() -> None: ...

class FMEPartIterator:
    """FME Part Iterator Class

    FMEPartIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEFeature to get an FMEPartIterator which can be used
    to iterate over its parts."""

    def __init__() -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def dimension() -> int:
        """Get the part's dimension. Returns either FME_TWO_D or FME_THREE_D.

        Returns:
            (int): The dimension of the part.
        """
    def getAllCoordinates() -> list[tuple[float]]:
        """Get all the part's coordinates in a list. Each coordinate is a tuple.

        All returned tuples have the same dimension as the part.

        Returns:
            (list[list[float]]): A list of the part's coordinates.
        """
    def getCoordinate(index: int) -> tuple[float]:
        """Get the coordinate at the specified index.

        The dimension of the tuple equals the dimension of the part.

        Args:
            index (int): The index at which the coordinate is retrieved.

        Returns:
            (tuple[float]): The coordinate at the given index.
        """
    def numVertices() -> int:
        """Get the number of vertices.

        Returns:
            (int): The number of vertices in the part.
        """

# Attribute types
FME_ATTR_BOOLEAN: int
FME_ATTR_ENCODED_STRING: int
FME_ATTR_INT16: int
FME_ATTR_INT32: int
FME_ATTR_INT64: int
FME_ATTR_INT8: int
FME_ATTR_LIST: int
FME_ATTR_REAL32: int
FME_ATTR_REAL64: int
FME_ATTR_REAL80: int
FME_ATTR_STRING: int
FME_ATTR_UINT16: int
FME_ATTR_UINT32: int
FME_ATTR_UINT64: int
FME_ATTR_UINT8: int
FME_ATTR_UNDEFINED: int

# Classic geometry types
FME_GEOM_AGGREGATE: int
FME_GEOM_DONUT: int
FME_GEOM_LINE: int
FME_GEOM_PIP: int
FME_GEOM_POINT: int
FME_GEOM_POLYGON: int
FME_GEOM_UNDEFINED: int

# Attribute casing: int
FME_NAME: int
FME_VALUE: int
FME_NAME_VAL: int
FME_ATTR_LIST
FME_UPPERCASE: int
FME_LOWERCASE: int
FME_TITLECASE: int
FME_FULLTITLECASE: int

# Dimensions
FME_TWO_D: int
FME_THREE_D: int

# Core format attributes
kFMEBasename: int
kFMEDataset: int

# OGC versions
ogcvOneDotOne: int
ogcvOneDotTwo: int
ogcvPostGISOneDotZero: int
ogcvPostGISOneWithSQLMM3: int
ogcvPostGISPreOneDotZero: int

# Serialize Options
kFME_FeatureSerializeOption: int
kFME_FeatureFullFeature: int
kFME_FeatureGeometry: int
kFME_FeatureSerializeExcludeAttr: int
kFME_FeatureSerializeSidecarBasename: int

# Deserialize Options: int
kFME_FeatureDeserializeOption: int
kFME_FeatureDeserializeReset: int
kFME_FeatureDeserializeMerge: int
kFME_FeatureDeserializeSidecarBasename: int

# General Processing Operations
kFME_ConvertToArea: int
kFME_PolygonDissolve: int
