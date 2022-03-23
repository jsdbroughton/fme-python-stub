from types import TracebackType
from typing import Any, overload
from six import text_type, string_types

# Versioning and metadata constants
FME_ASSEMBLY_VERSION: str
"""e.g. “2018.7.34.18078”"""
FME_BUILD_DATE: str
"""e.g. “20170421”"""
FME_BUILD_NUM: str
"""e.g. “18078”"""
FME_BUILD_STRING: str
"""e.g. “20170421 - Build 18078 - WIN64”"""
FME_COMPANY: str
"""“Safe Software Inc.”"""
FME_COPYRIGHT: str
"""e.g. “Copyright (c) 1994 - 2017, Safe Software Inc.”"""
FME_DLL_VERSION: str
"""e.g. “2018, 7, 34, 18078”"""
FME_MAJOR_PRODUCT_NAME: str
"""e.g. “FME(R) 2018.0”"""
FME_PRODUCT_NAME: str
"""e.g. “FME(R) 2018.0.0.0”"""

class FMEFeature:
    """FME Feature Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEFeature constructor

        Returns:
            FMEFeature: An instance of a Feature object."""
    @overload
    def __init__(self, feature: FMEFeature) -> None:
        """Creat a copy of the passed in Feature object.

        Args:
            feature (FMEFeature): The feature to copy.

        Returns:
            FMEFeature: An instance of a Feature object."""
    def addCoordinate(self, x: float, y: float, z: float = ...) -> None:
        """Add a coordinate to the part.

        If the feature is two-dimensional, any provided third coordinate is ignored.

        Args:
            x (float): The x coordinate.
            y (float): The y coordinate.
            z (float): The z coordinate.
        """
    def addCoordinates(self, coordinates: list[tuple[float, float, float]]) -> None:
        """Adds coordinates onto the feature.

        Missing values are replaced by 0. If the feature is two-dimensional, any provided third coordinate is ignored.

        Args:
            coordinates (list[tuple[float,float,float]]): The list of coordinates.
        """
    def boundingBox(self) -> list[list[float]]:
        """Get the bounding box of the feature.

        Returns:
            (list[list[float]]): The bounding box of the feature, in the
                form ((minx, miny), (maxx, maxy)).

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def boundingCube(
        self,
    ) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """Get the bounding cube of the feature.

        Returns:
            (tuple[tuple[float,float,float],tuple[float,float,float]]): The bounding
                cube of the feature, in the form ((minx, miny, minz), (maxx, maxy, maxz)).

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def buffer(self, width: float, sampleAngle: float) -> None:
        """This method generates a buffer around the feature.

        The features geometry is replaced by the new buffer geometry. If the feature
        is an area feature then the buffer is only generated on the outside (and
        inside holes) of the feature.

        Args:
            width (float): The number of ground units to buffer around the feature.
            sampleAngle (float): The sampling angle. If 5 then there is a vertex
                on the buffer every 5 degrees.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def buildAggregateFeat(self, featureList: list[FMEFeature]) -> None:
        """Build an aggregate feature from a list of features.

        Args:
            featureList (list[FMEFeature]): The list of features to aggregate.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def changeCase(
        self, changeOpt: int, matchExp: str or list[str], caseTpe: int
    ) -> None:
        """Change the letter case of attribute names and values.

        Args:
            changeOpt (int): The change option.
            matchExp (str or list[str]): The match expression.
            caseTpe (int): The new case to change the letters of the attribute
                names and values to.

                Must be one of:
                - FME_UPPERCASE
                - FME_LOWERCASE
                - FME_TITLECASE
                - FME_FULLTITLECASE
        Raise:
            FMEException: An exception is raised if an error occurred.
        """
    def chopUp(self, vertexThreshold: int) -> bool:
        """Convert a feature into an aggregate where each member of the aggregate
        has fewer than the threshold number of vertices.

        If the feature was an area based feature, it will do area chopping,
        subdividing the area so that no area piece has more than the number of
        vertices.

        If the feature was linear, then the line is broken into chunks that meet
        the size criteria.

        Args:
            vertexThreshold (int): The threshold number of vertices.

        Returns:
            bool: True if the feature was chopped up, False otherwise.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def cloneAttributes(self) -> FMEFeature:
        """Create a new FMEFeature with only the attributes of this one copied over.

        Returns:
            FMEFeature: A new FMEFeature with the same attributes as the original.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertAnyArcToPoints(
        self,
        center: tuple[float, float],
        semiPrimaryAxis: float,
        semiSecondaryAxis: float,
        origNumSamps: int,
        startAngle: float,
        sweepAngle: float,
        rotation: float,
    ) -> None:
        """Strokes an arc feature to be a points.

        Args:
            center (tuple[float,float]): The center of the arc.
            semiPrimaryAxis (float): The semi-primary axis of the arc.
            semiSecondaryAxis (float): The semi-secondary axis of the arc.
            origNumSamps (int): The number of samples to use.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.
            rotation (float): The rotation of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertArcToPointUseAttributes(self) -> None:
        """Return the bounding cube of the feature in the format ((min x, min y,
        min z), (max x, max y, max z)) Strokes an arc feature to be a polygon or
        line. The parameters used to stroke the arc or ellipse are retrieved from
        the related attributes. Arcs with a sweep angle of 360 degrees will be
        converted into a polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertArcToPoints(
        self,
        center: tuple[float, float],
        semiPrimaryAxis: float,
        semiSecondaryAxis: float,
        origNumSamps: int,
        startAngle: float,
        sweepAngle: float,
        rotation: float,
    ) -> None:
        """Strokes an arc feature to be a polygon or line.

        Args:
            center (tuple[float,float]): The center of the arc.
            semiPrimaryAxis (float): The semi-primary axis of the arc.
            semiSecondaryAxis (float): The semi-secondary axis of the arc.
            origNumSamps (int): The number of samples to use.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.
            rotation (float): The rotation of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertPointsToArc(
        self, radiusAttrName: str, startAngleAttrName: str, sweepAngleAttrName: str
    ) -> None:
        """Converts the feature into a point feature with attributes required to
        define it as an arc. If the feature has more than 3 points, the arc is
        approximated.

        Args:
            radiusAttrName (str): The attribute name of the radius.
            startAngleAttrName (str): The attribute name of the start angle.
            sweepAngleAttrName (str): The attribute name of the sweep angle.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def deserialize(self, buffer: bytearray, parameters: dict[str, str]) -> bool:
        """Restore the state of the FMEFeature from the specified buffer.

        Args:
            buffer (bytearray): The buffer from which the state of the feature is
                restored from.
            parameters (dict[str,str]): (Optional) Possible name-value pairs are:

                - kFME_FeatureDeserializeOption:
                    - kFME_FeatureDeserializeReset: (Default) Reset the original
                    feature before restoring the state of the FMEFeature.
                    - kFME_FeatureDeserializeMerge: When restoring the state of
                    the FMEFeature, the original feature will NOT be reset; the
                    original information in the feature will be preserved when
                    there is no corresponding information in the buffer. Attributes,
                    geometry, coordinate system information, etc. taken from the
                    buffer will overwrite such information on the feature if necessary.
                - kFME_FeatureDeserializeSidecarBasename:
                    File from which to read extra geometry data: The path and
                    basename (not including file extension) from which additional
                    data will be read for some geometries (raster, point cloud).
                    If this option is not specified for those geometries, they
                    may return an error when data is requested (e.g. when writing
                    out a raster).

        Returns:
            bool: True on success, False otherwise.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def exportGeometryToOGCWKB(self, version: int) -> bytearray or bytes or None:
        """Convert the geometry of the feature to the OGC Well Known Binary format.

        Args:
            version (int): Optional) The OGC Version to use. Must be one of:
                - ogcvOneDotOne (default)
                - ogcvOneDotTwo
                - ogcvPostGISPreOneDotZero
                - ogcvPostGISOneDotZero
                - ogcvPostGISOneWithSQLMM3

        Returns:
            bytearray or bytes or None: A buffer representing the geometry of the
                feature converted to the OGCWKB.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def exportGeometryToOGCWKT(self, version: int) -> str:
        """Convert the geometry of the feature to the OGC Well Known Text format.

        Args:
            version (int): Optional) The OGC Version to use. Must be one of:
                - ogcvOneDotOne (default)
                - ogcvOneDotTwo
                - ogcvPostGISPreOneDotZero
                - ogcvPostGISOneDotZero
                - ogcvPostGISOneWithSQLMM3

        Returns:
            str: A string representing the geometry of the feature converted
                to the OGCWKT.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def generatePointInPolygon(self, pretty: bool) -> tuple[float, float, float]:
        """Generate a point somewhere inside the polygon.

        If the feature is 3D, the Z value is calculated to be the average of all
        points on the feature.

        Args:
            pretty (bool): (Optional) Generate a point that has a more central
                position, however more computational time may be required (default
                is False).

        Returns:
            tuple[float,float,float]: A point somewhere inside the polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAllAttributeNames(self) -> list[str]:
        """This method returns a complete, exhaustive list of all the attribute
        names present in the feature.

        Returns:
            list[str]: A list of all attribute names.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAllCoordinates(self) -> list[tuple[float, float, float]]:
        """Get all the coordinates in this feature.

        Returns a list of coordinates, each as a tuple of floats.

        Returns:
            list[tuple[float,float,float]]: A list of all coordinates.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAttribute(
        self,
        attrName: str,
        desiredType: type,
        fallback: bool
        or int
        or float
        or str
        or bytes
        or bytearray
        or list[Any]
        or None,  # ignore
    ) -> bool or int or float or str or bytes or bytearray or list[Any] or None:
        """Get the value of an attribute.

        Args:
            attrName (str): The name of the attribute.
            desiredType (type): (Optional) The desired type for the attribute value
                to be returned as. Possible values are bool, int, float, str, bytes,
                bytearray, and list.
            fallback (bool): (Optional) If specified, this value is returned
                instead of raising FMEException on conversion failures.

        Returns:
            bool or int or float or str or bytes or bytearray or list[Any] or None:
                The value of the attribute.

        Raises:
            FMEException: An exception is raised if there was a problem in retrieving
                the attribute value.
        """
    def getAttributeAsType(
        self, attrName: str, attrType: int, fallback: Any
    ) -> bool or int or float or str or list[str] or bytearray or list[
        bytearray
    ] or bytes or list[bytes] or None:
        """[DEPRECATED] Get the value of the named attribute, casted to the specified
        FME type, then to an appropriate python type.

        An optional third parameter can be specified to be returned as a fallback
        in case type conversion fails.

        Example: getAttributeAsType(“output_file_type”, fmeobjects.FME_ATTR_STRING, “png”)

        The enum value fmeobjects.FME_ATTR_UNDEFINED can be used to retrieve a list
        object. If used to try and get a single attribute as a list, or a list as
        a single type, there is automatic conversion failure.

        A return of None indicates the attribute does not exist.

        Args:
            attrName (str): The name of the attribute.
            attrType (int): The type of the attribute.
            fallback (Any): (Optional) If specified, this value is returned instead
                of raising FMEException on conversion failures.

        Returns:
            bool or int or float or str or bytes or bytearray or list[Any] or None:
                The value of the attribute.

        Raises:
            FMEException: An exception is raised if there was a problem in retrieving
                or converting the attribute value.
        """
    def getAttributeNullMissingAndType(
        self, attributeName: str
    ) -> tuple[bool, bool, int]:
        """[DEPRECATED] This method returns a tuple of a boolean indicating if the
        attribute is null, a boolean indicating if the attribute is missing, and
        an integer representing the type of the attribute.

        The first boolean is True if attributeName maps to a null attribute value
        on the feature. Otherwise it is False. The second boolean is True if
        attributeName maps to no value on the feature. Otherwise it is False. If
        the attribute is absent, FME_ATTR_UNDEFINED is returned for the type,
        otherwise the attribute type is returned.

        Args:
            attributeName (str): The name of the attribute.

        Returns:
            tuple[bool, bool, int]: A tuple of 2 boolean values and an integer.
                The first boolean indicating whether or not the value of the
                attribute is null, the second boolean indicating whether or not
                the attribute is missing, and the integer representing the
                attribute type. Attribute type int values are represented by the
                constants FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN, FME_ATTR_INT8,
                FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16, FME_ATTR_INT32,
                FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64, FME_ATTR_REAL80,
                FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64,
                or FME_ATTR_UINT64."""
    def getAttributeType(self, attrName: str) -> int:
        """Get the type of the named attribute.

        Args:
            attrName (str): The name of the attribute.

        Returns:
            int: The type of the attribute. Attribute type int values are
                represented by the constants FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
                FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
                FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
                FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING,
                FME_ATTR_INT64, or FME_ATTR_UINT64."""
    def getCoordSys(self) -> str:
        """Get the coordinate system of the feature.

        Returns:
            str: The coordinate system of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getCoordinate(self, index: int) -> tuple[float, float, float]:
        """Access the feature's individual coordinates by index.

        The index must be in the range 0 .. ( numCoords() - 1).

        Args:
            index (int): The index of the coordinate.

        Returns:
            tuple[float,float, float]: The coordinate at the specified index.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getDimension(self) -> int:
        """Get the dimension of the feature.

        Returns either FME_TWO_D or FME_THREE_D

        Returns:
            int: The dimension of the feature."""
    def getDonutParts(self) -> list[FMEFeature]:
        """Break a donut feature into its constituent parts. The first part is
        the outer shell of the donut polygon, and the following parts are the
        holes. All of the parts have the same attributes and feature type as the
        original feature.

        Returns:
            list[FMEFeature]: The donut parts of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getFeatureType(self) -> str:
        """Get the feature type of the feature.

        Returns:
            str: The feature type of the feature."""
    def getGeometry(self) -> FMEGeometry:
        """Get the geometry of the feature.

        Returns:
            FMEGeometry: The geometry of the feature. Note: This method returns
                a terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMEPoint is returned if the geometry truly is a point."""
    def getGeometryType(self) -> int:
        """Get the geometry type of the feature.

        Returns:
            int: The geometry type of the feature. Returns one of FME_GEOM_UNDEFINED,
            FME_GEOM_POINT, FME_GEOM_LINE, FME_GEOM_POLYGON, FME_GEOM_DONUT,
            FME_GEOM_PIP, or FME_GEOM_AGGREGATE."""
    def getSequencedAttributeNames(self) -> list[str]:
        """This method gets a list of sequenced attribute names in the order they
        were added to the feature.

        The attrNames list is only populated for schema features. The list will
        not contain sequenced attribute names for data features.

        Returns:
            list[str]: The names of the attributes in the feature."""
    def hasGeometry(self) -> bool:
        """[DEPRECATED] Check if the feature has a geometry.

        Returns:
            bool: True if the feature has a geometry, False otherwise."""
    def hasRichGeometry(self) -> bool:
        """Determine if the feature has geometry that takes advantage of the new
        geometry technology.

        Returns:
            bool: True if the feature's geometry takes advantage of the new
                geometry technology, and False otherwise."""
    def importGeometryFromOGCWKB(self, ogcwkb: bytearray) -> None:
        """Set the geometry of the feature to be that specified in the OGC Well
        Known Binary format. If the feature has geometry, then the geometry is
        replaced.

        Args:
            ogcwkb (bytearray): Specifies the geometry of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def importGeometryFromWKT(self, ogcwkt: str) -> None:
        """Set the geometry of the feature to be that specified in the Well
        Known Text format. If the feature has geometry, then the geometry is
        replaced.

        Args:
            ogcwkt (str): Specifies the geometry of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def interpolateSpline(
        self, numPointsPerSegment: int, calcPhantomPoints: bool
    ) -> None:
        """Perform interpolation on the feature.

        Args:
            numPointsPerSegment (int): The number of points per segment.
            calcPhantomPoints (bool): If True, phantom points are calculated.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isAttributeMissing(self, attributeName: str) -> bool:
        """This method returns a boolean indicating if the attribute name maps to
        no value on the feature.

        Args:
            attributeName (str): The name of the attribute.

        Returns:
            bool: True if the attribute is missing, False otherwise.
        """
    def isAttributeNull(self, attributeName: str) -> bool:
        """This method returns a boolean indicating if the attribute name maps to
        a null value on the feature.

        Args:
            attributeName (str): The name of the attribute.

        Returns:
            bool: True if the attribute is null, False otherwise.
        """
    def makeDonuts(self, featureList: list[FMEFeature]) -> None:
        """Construct a donut polygon from the list of features provided. If multiple
        donut polygons are formed then the resulting geometry is an aggregate of
        these donuts.

        Args:
            featureList (list[FMEFeature]): The list of features to make the donut from.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def matrixTransform(self, matrix: list[list[float]]) -> None:
        """Transform the feature using a matrix.

        Args:
            matrix ((float, float), (float, float)) or
                ((float, float, float), (float, float, float), (float, float, float))):
                    The matrix to transform the feature with.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def mergeAttribute(self, destFeature: FMEFeature) -> None:
        """Set the featureType and attributes of the feature passed in from the
        current feature, but ONLY if those attributes are not already present.

        The geometry is not touched. The original attributes on the destFeature
        are not lost.

        Args:
            destFeature (FMEFeature):  The original feature to set featureType
                and attributes on.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def numCoords(self) -> int:
        """Get the number of coordinates in the feature.

        We recommend limited use of this method since it returns numVertices() +
        numParts() for multi-part features. A true vertex count will be returned
        by numVertices().

        Returns:
            int: The number of coordinates in the feature."""
    def numParts(self, flatten: bool, splitDonuts: bool) -> int:
        """Get the number of parts in the feature.

        Args:
            flatten (bool):  If flatten is True, then return the number of primitive
                parts drilling down into sub aggregates. If flatten is False then
                it returns the number of high level parts with some parts potentially
                being aggregates.
            splitDonuts (bool): If splitDonuts is True, each ring of a donut will
                count as a separate part.

        Returns:
            int: The number of parts in the feature."""
    def numVertices(self) -> int:
        """Get the number of vertices that make up the geometry of the feature
        Multi-part (aggregate) geometries are handled properly.

        For simple geometries, the same value is returned as in numCoords()

        Returns:
            int: The number of vertices in the feature."""
    def offset(self, x: float, y: float, z: float) -> None:
        """Offset the feature by the specified amount.

        Args:
            x (float): The amount to offset the feature in the x direction.
            y (float): The amount to offset the feature in the y direction.
            z (float): The amount to offset the feature in the z direction.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def orient(self, rule: int) -> int:
        """Optionally set and get the orientation rule of the feature.

        This descends into aggregates and orients any polygons or donuts found.
        Geometries other than polygons or donuts are left unchanged.

        Args:
            rule (int): (Optional) If the parameter is not supplied, the orientation
                is not changed. If the rule is supplied, the feature is adjusted
                so that rule is followed.

                With the right hand rule, the area of the polygon is always on the
                right and the coordinates of the outer boundary are in the clockwise
                direction, and for any holes they are counterclockwise.

        Returns:
            int: The orientation rule of the feature.
        """
    def outerShell(self) -> None:
        """Set the geometry of the feature to be just its outer shell. This has
        no effect on non-area features.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def performFunction(self, functionSpecification: str) -> str:
        """Call an FME function on the feature. See the FME Factory and Function
        Documentation for formatting and the list of supported functions. It may
        not support newer FME functions. Functions that are not supported will
        produce an error message indicating that the function is not recognized.
        The function string passed in to this function follows the syntax of the
        documentation exactly.

        i.e. feature.performFunction('@Count()')

        Note that no spaces should be present between any parameters of the function,
        or between the function name and the '('. Additionally, do not call this
        method during a writer's close() method.

        Args:
            functionSpecification (str): The function specification.

        Returns:
            str: The result of the function.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def processFeature(
        self, featureList: list[FMEFeature], paramList: list[str]
    ) -> None:
        """Perform some general processing operation on a list of features.

        The operation performed is governed by the contents of paramList.

        Args:
            featureList (list[FMEFeature]): The list of features to process.
            paramList (list[str]): The first entry in the array determines the
                type of operation.

                The following types of operations are supported:

                - kFME_ConvertToArea: The contents of the feature list are assumed
                to be a collection of lines. These lines are then formed into
                polygons. The polygons which result are turned into donuts and
                aggregated. Any holes are themselves dropped from the result. The
                single resulting area geometry is applied to the current feature.
                - kFME_PolygonDissolve: The contents of the feature list are
                assumed to be a collection of polygons. If there are non-polygon
                features, then they will be filtered out. The collection of polygon
                features will be dissolved and the result will be applied to the
                current feature. Dissolved polygons are those polygons formed when
                shared edges between adjacent polygons are removed. This operation
                assumes that all input polygons are properly noded, a vertex is
                present at each intersection point, and that polygons are not
                overlapping.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeAttribute(self, attrName: str) -> None:
        """Remove an attribute from the feature.

        Args:
            attrName (str): The name of the attribute to remove."""
    def removeAttrsWithPrefix(self, attrPrefix: str) -> None:
        """Remove all attributes from the feature that have a name that starts
        with the specified prefix.

        Args:
            attrPrefix (str): The prefix to remove."""
    def removeGeometry(self) -> FMEGeometry:
        """Remove and return the feature's geometry.

        The feature loses its geometry and it can no longer be accessed.

        Returns:
            FMEGeometry: The geometry of the feature. Note: This method returns
                a terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMEPoint is returned if the geometry truly is a point."""
    def removeTraits(self, regexp: str) -> None:
        """Remove all traits from the feature that match the specified regular
        expression.

        Args:
            regexp (str): (Optional) All traits matching this regular expression
                are removed. If no expression is supplied, all traits are removed."""
    def reproject(self, coordSys: str) -> None:
        """Reproject the feature from its current coordinate system to that specified.

        If the feature has no coordinate system specified then this has the same
        effect as the setCoordSys method.

        Args:
            coordSys (str): The coordinate system to set on the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def resetCoords(self) -> None:
        """Reset the number of coordinates in the feature to 0."""
    def resetFeature(self) -> None:
        """Reset (clear) all the attributes and geometry of the feature.

        It results in a fresh clean feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def rotate2D(self, origin: tuple[float, float], angle: float) -> None:
        """Rotate the feature counterclockwise around the origin point by the
        specified angle (in degrees).

        Args:
            origin (tuple[float, float]): The origin of the rotation.
            angle (float): The angle (in degrees) which to rotate the feature in
                the counterclockwise direction.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, x: float, y: float, z: float) -> None:
        """Scale the feature by the specified amount.  (2D or 3D)

        Args:
            x (float): The amount to scale the feature in the x direction.
            y (float): The amount to scale the feature in the y direction.
            z (float): (Optional) The value to scale z by. (Default value is 1.0)

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def serialize(self, parameters: dict[str, str]) -> bytearray or bytes or None:
        """Write the state of the FMEFeature to a string buffer.

        Args:
            parameters (dict[str,str]): (Optional) Possible name-value pairs are:

                - kFME_FeatureSerializeOption:
                    - kFME_FeatureFullFeature: (Default) Serialize the full full
                    feature.
                    - kFME_FeatureGeometry: Serialize the geometry portion of a
                    feature only. This includes coordinates, coordinate system,
                    and geometry attributes.
                - kFME_FeatureSerializeExcludeAttr:
                    - Attribute names to exclude: The names of the attributes to
                    exclude when doing feature serialization. The value can be a
                    single string or a list.
                - kFME_FeatureSerializeSidecarBasename:
                    - File in which to store extra geometry data: The path and
                    basename (not including file extension) to which additional
                    data will be written for some geometries (raster, point cloud).
                    If this option is not specified for those geometries, the
                    extra data will not be written.

        Returns:
            bytearray or bytes or None: The serialized feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setAttribute(
        self,
        attrName: str,
        attrValue: bool
        or int
        or str
        or list[str]
        or float
        or bytearray
        or list[bytearray]
        or bytes
        or list[bytes],
    ) -> None:
        """Set the value of an attribute.

        If the attribute already exists, it will be overwritten. The following
        type numeric mappings are used:
            PyInt ==> FME_Int32
            PyFloat ==> FME_Real64
            PyLong ==> FME_Int64

        Binary values are to be specified as bytes or bytearray values.

        If an attribute value of None is specified, the attribute value will be
        set as an empty string. To set a null attribute, use setAttributeNullWithType.

        For a list attribute, if the attribute already exists and contains more
        elements than the new list, the resulting list will be made up of the new
        list elements plus the old list elements that were not overwritten. Call
        removeAttribute first to avoid this behavior.

        Args:
            attrName (str): The name of the attribute to set.
            attrValue (bool or int or str or list[str] or float or bytearray or
                list[bytearray] or bytes or list[bytes]): The value of the attribute.
        """
    def setAttributeNullWithType(self, attrName: str, attrType: int) -> None:
        """This method supplies a null attribute with a type to the feature.

        If an attribute with the same name already exists, it is overwritten.

        Attribute type must be one of: FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
        FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
        FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
        FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING,
        FME_ATTR_INT64 or FME_ATTR_UINT64.

        Args:
            attrName (str): The name of the attribute to set.
            attrType (int): An integer representing the attribute type.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setCoordSys(self, coordSys: str) -> None:
        """Set the coordinate system of the feature.

        Args:
            coordSys (str): The coordinate system to set on the feature.
        """
    def setDimension(self, dimension: int) -> None:
        """Set the dimension of the feature.

        Dimension must either be FME_TWO_D or FME_THREE_D

        Args:
            dimension (int): The dimension to set on the feature.
        """
    def setFeatureType(self, featureType: str) -> None:
        """This method sets the feature type of the FMEFeature.

        The feature type is often also called the “class” or “category” of the
        feature. The feature type set on a feature through this method will change
        as the feature is routed through a translation pipeline.

        Args:
            featureType (str): The feature type to set on the feature.
        """
    def setGeometry(self, geometry: FMEGeometry) -> None:
        """Set the geometry of the feature.

        Any existing geometry on the feature is overwritten.

        Args:
            geometry (FMEGeometry): The geometry to set on the feature.
        """
    def setGeometryType(self, geomType: int) -> None:
        """Set the feature's classic geometry type.

        geomType must one of: FME_GEOM_UNDEFINED, FME_GEOM_POINT, FME_GEOM_LINE,
        FME_GEOM_POLYGON, FME_GEOM_DONUT, FME_GEOM_PIP, or FME_GEOM_AGGREGATE.

        Args:
            geomType (int): The geometry to set on the feature.
        """
    def setSequencedAttribute(self, attrName: str, attrValue: str or list[str]) -> None:
        """Supply a new attribute for the feature, but in such a way that the sequence
        is remembered.

        This is needed for schema features, to preserve the order of attributes.

        For a list attribute, if the attribute already exists and contains more
        elements than the new list, the resulting list will be made up of the new
        list elements plus the old list elements that were not overwritten. Call
        removeAttribute first to avoid this behavior.

        Args:
            attrName (str): The name of the attribute to set.
            attrValue (str or list[str]): The value of the attribute.
        """
    def splitAggregate(self, recurse: bool) -> list[FMEFeature]:
        """Split up an aggregate feature into pieces, all of which have the same
        attributes and feature type. If the recurse flag is True, all aggregates
        within the aggregate are also split recursively, so no aggregates are ever
        returned as pieces. This method will only return points, lines, polygons,
        and null geometries (and possibly aggregates if recurse is False). All
        other geometries will be converted to these when split.

        Args:
            recurse (bool): (Optional) Whether to recursively split the aggregate
            until no aggregates remain. (Default value is False)

        Returns:
            list[FMEFeature]: A list of features resulting from the splitting of the original aggregate.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEPartIterator:
    """FME Part Iterator Class

    FMEPartIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEFeature to get an FMEPartIterator which can be used
    to iterate over its parts."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def dimension(self) -> int:
        """Get the part's dimension. Returns either FME_TWO_D or FME_THREE_D.

        Returns:
            (int): The dimension of the part.
        """
    def getAllCoordinates(self) -> list[tuple[float]]:
        """Get all the part's coordinates in a list. Each coordinate is a tuple.

        All returned tuples have the same dimension as the part.

        Returns:
            (list[list[float]]): A list of the part's coordinates.
        """
    def getCoordinate(self, index: int) -> tuple[float]:
        """Get the coordinate at the specified index.

        The dimension of the tuple equals the dimension of the part.

        Args:
            index (int): The index at which the coordinate is retrieved.

        Returns:
            (tuple[float]): The coordinate at the given index.
        """
    def numVertices(self) -> int:
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
FME_ATTR_LIST: int
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

# Library Types
FME_LIB_APPEARANCE: int
FME_LIB_TEXTURE: int
FME_LIB_RASTER: int
FME_LIB_GEOMETRY_DEFINITION: int

# Mapper Types
FME_MAPPER_ALPHA_MAP: int
FME_MAPPER_ALPHA_MASK: int
FME_MAPPER_AMBIENT_MAP: int
FME_MAPPER_AMBIENT_MASK: int
FME_MAPPER_DIFFUSE_MAP: int
FME_MAPPER_DIFFUSE_MASK: int
FME_MAPPER_EMISSIVE_MAP: int
FME_MAPPER_EMISSIVE_MASK: int
FME_MAPPER_SHININESS_MAP: int
FME_MAPPER_SHININESS_MASK: int
FME_MAPPER_SPECULAR_MAP: int
FME_MAPPER_SPECULAR_MASK: int
FME_MAPPER_BUMP_MAP: int
FME_MAPPER_BUMP_MASK: int

# Texture Wrap Methods
FME_TEXTURE_REPEAT_BOTH: int
FME_TEXTURE_CLAMP_BOTH: int
FME_TEXTURE_CLAMP_U_REPEAT_V: int
FME_TEXTURE_REPEAT_U_CLAMP_V: int
FME_TEXTURE_MIRROR: int
FME_TEXTURE_BORDER_FILL: int
FME_TEXTURE_NONE: int

class FMETexture:
    """FME Texture Class"""

    def __init__(self) -> None:
        """Create an instance of a blank texture object."""
    def clone(self) -> "FMETexture":
        """Clone the texture object.

        Returns:
            FMETexture: A new texture object.
        """
    def getBorderColors(self) -> tuple[float, float, float]:
        """This routine retrieves the border color of this Texture.

        The color is a vector in r g b color space with values between 0.0 and 1.0.
        This will return None if it did not have a border color set.

        Returns:
            tuple[float,float,float]: The border color, formatted (ddd) (r, g, b).
        """
    def getCenter(self) -> tuple[float, float] or None:
        """This routine retrieves the center associated with the texture.

        This will return None if the center is the default center of (0,0).
        The center is only used for shearing and rotation.

        Returns:
            tuple[float,float]: The center, formatted (dd) (u, v).
        """
    def getOffset(self) -> tuple[float, float] or None:
        """This routine retrieves the offset associated with the texture.

        This will return None if the offset is the default offset of (0,0).
        The offset is only used for translation.

        Returns:
            tuple[float,float]: The offset, formatted (dd) (u, v).
        """
    def getRotation(self) -> int or None:
        """This routine retrieves the rotation angle associated with the texture.

        The angle is stored in degrees CCW from the x-axis, and is by default 0.
        Rotation is centered according to the Center variable. This return None
        if the scaling is the default angle of 0.

        Returns:
            int: The rotation, in degrees.
        """
    def getScaling(self) -> tuple[float, float] or None:
        """This routine retrieves the scaling factors associated with the texture.

        This will return None if the scaling is the default scaling of (1,1).

        Returns:
            tuple[float,float]: The scaling factors, formatted (dd) (u, v), or None.
        """
    def getShear(self) -> tuple[float, float] or None:
        """This routine retrieves the shear factors associated with the texture.

        Shearing is centered according to the Center variable. This will return
        None if the shearing is the default shearing of (0,0).

        Returns:
            tuple[float,float]: The shear factors, formatted (dd) (u, v), or None.
        """
    def getTextureWrap(self) -> int:
        """This routine retrieves the wrapping style associated with the texture.

        The style is stored as a Texture Wrap value, and is by default
        FME_TEXTURE_REPEAT_BOTH, which results in the texture being tiled in
        both the u and v direction.

        Returns:
            int: The texture wrap mode.
        """
    def getTransformationMatrix(self) -> list[list[float]]:
        """This routine retrieves the transformation matrix associated with the texture.

        It is a combination of the rotation, scaling, shear and translation factors,
        applied in that order.

        Returns:
            list[list[float]]: The texture's tranformation matrix, formatted [[ddd][ddd]].
        """
    def getTransformationMatricReverse(self) -> list[list[float]]:
        """This routine retrieves the texture transformation matrix associated with
        the texture in the reverse order and inverse of each operation, that
        consists of offset, negative shear, 1 / scale, and negative rotation in that order.

        This matrix can be used to transform the texture coordinates that are
        associated with this texture.

        Returns:
            list[list[float]]: The texture's tranformation matrix, formatted [[ddd][ddd]].
        """
    def hasNonIdentityTransform(self) -> bool:
        """This routine returns True if any non-default texture transform factors are set.

        The default texture transform matrix is identity and this returns False.

        Returns:
            bool: Returns True if any non-default texture transform factors are
                set, or False otherwise.
        """
    def setBorderColors(self, r: float, g: float, b: float) -> None:
        """This routine sets the border color of this Texture.

        The color values should be in r g b color space with values between 0.0
        and 1.0. The border color is used only if the Texture Wrap value is set
        to FME_TEXTURE_BORDER_FILL. Setting the border color will also set the
        Texture Wrap value to FME_TEXTURE_BORDER_FILL. Setting the any color
        value to a negative value will remove the color from this Texture and the
        Texture Wrap value will be reset to FME_TEXTURE_REPEAT_BOTH. If the
        underlying raster is single channel, the gray-scale equivalent border
        color will be calculated.

        Args:
            r (float): The red value.
            g (float): The green value.
            b (float): The blue value.
        """
    def setCentre(self, u: float, v: float) -> None:
        """This routine sets the center associated with the texture.

        he default center for a texture is (0,0). The center is only used for
        shearing and rotation.

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setOffset(self, u: float, v: float) -> None:
        """This routine sets the offset associated with the texture.

        The default offset for a texture is (0,0).

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setRotation(self, angle: float) -> None:
        """This routine sets the rotation angle associated with the texture.

        Rotation is centered according to the Center variable. The angle is
        stored in degrees CCW from the x-axis, and is by default 0.

        Args:
            angle (int): The angle, in degrees.
        """
    def setScaling(self, u: float, v: float) -> None:
        """This routine sets the scaling factors associated with the texture.

        The default scaling for a texture is (1,1).

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setShear(self, u: float, v: float) -> None:
        """This routine sets the shear factors associated with the texture.

        The default shear for a texture is (0,0).

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setTextureWrap(self, wrapStyle: int) -> None:
        """This routine sets the wrapping style associated with the texture.

        The style is stored as a Texture Wrap value. If the style is set to
        FME_TEXTURE_BORDER_FILL, the default border color of black (0,0,0), will
        be set. If the style is set to something other than FME_TEXTURE_BORDER_FILL,
        the border color will be removed from the texture.

        Args:
            wrapStyle (int): The wrapping style associated with the texture.
                One of : FME_TEXTURE_BORDER_FILL, FME_TEXTURE_REPEAT_BOTH,
                FME_TEXTURE_CLAMP_BOTH, FME_TEXTURE_CLAMP_U_REPEAT_V,
                FME_TEXTURE_REPEAT_U_CLAMP_V, FME_TEXTURE_MIRROR, FME_TEXTURE_NONE.
        """
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """This routine sets the transformation matrix associated with the texture.

        The shear, offset, rotation and will be calculated from the matrix so
        that when rotation, shear, scale and translation are applied in order,
        it is the equivalent of the input matrix. If the non-translation component
        of the matrix has a zero determinant or m[0][0] = 0, the matrix will not
        be used and existing parameters will remain unchanged.

        Args:
            matrix (list[list[float]]): The transformation matrix,
                formatted [[ddd][ddd]].
        """

class FMELibraryIterator:
    """FME Library Iterator Class

    FMELibraryIterator should not be constructed directly. Instead, use the
    iterator semantics of FMELibrary to get an FMELibraryIterator which can be
    used to iterate over its librarys."""

    def __init__(self) -> None:
        """Constructor for FMELibraryIterator."""
    def getAppearance(self) -> FMEAppearance or None:
        """This method returns a copy of the current shared object as an appearance
        if getType() returns FME_LIB_APPEARANCE. Otherwise, it returns None.

        Returns:
            FMEAppearance: The current object's appearance.
        """
    def getAsTexture(self) -> FMETexture or None:
        """This method returns a copy of the current shared object as a texture
        if getType() returns FME_LIB_TEXTURE. Otherwise, it returns None.

        Returns:
            FMETexture: The current object's texture.
        """
    def getReference(self) -> int:
        """Returns the object's reference from the FMELibrary.

        Returns:
            int: The current object's reference.
        """
    def getType(self) -> int:
        """Returns the type of the current object.

        Returns:
            int: The object's type. Must be either: FME_LIB_APPEARANCE,
                FME_LIB_TEXTURE, FME_LIB_RASTER, or FME_LIB_GEOMETRY_DEFINITION.
        """

class FMELibrary:
    """FME Library Class

    Contains shared objects used by multiple features. Appearances and textures
    for all features are stored in this library."""

    def __init__(self) -> None:
        """Constructor for FMELibrary."""
    def addAppearance(self, appearance: FMEAppearance) -> int:
        """This routine adds the appearance object to the Library.

        If the appearance passed in is None, this appearance is will not be added
        to the Library. There is no checking for duplicates when adding an
        appearance. This call will always add the appearance to the Library,
        even if an identical appearance already exists therein. If the addition
        is successful, the method returns a unique appearance reference 'key' that
        is associated with the appearance. If there are any errors in operation,
        an exception is raised. If the appearance is successfully added to the
        library, the library consumes the appearance.

        Args:
            appearance (FMEAppearance): The appearance to add.

        Returns:
            int: The unique appearance reference 'key'.

        Raises:
            FMEException: If there is an error adding the appearance.
        """
    def addGeometryDefinition(self, geometryDef: FMEGeometry) -> int:
        """This routine adds the geometry definition object to the Library.

         If the Geometry Definition passed in is None, this Geometry Definition
         will not be added to the Library. There is no checking for duplicates
         when adding a Geometry Definition. This call will always add the Geometry
         Definition to the Library, even if an identical one already exists therein.
         If there are any errors in operation an exception is raised. If the
         addition is successful, a unique geometry definition reference 'key' that
         is associated with the Geometry Definition is returned.

        Args:
            geometryDef (FMEGeometry): The geometry definition to add.

        Returns:
            int: The unique geometry definition reference 'key'.

        Raises:
            FMEException: If there is an error adding the geometry definition.
        """
    def addTexture(self, texture: FMETexture) -> int:
        """This routine adds the texture object to the Library.

        If the texture passed in is None, this texture is will not be added to
        the Library. There is no checking for duplicates when adding a texture.
        This call will always add the texture to the Library, even if an identical
        texture already exists therein. If there are any errors in operation, an
        exception is raised. If the addition is successful, the method returns a
        unique texture reference 'key' that is associated with the texture.

        Args:
            texture (FMETexture): The texture to add.

        Returns:
            int: The unique texture reference 'key'.

        Raises:
            FMEException: If there is an error adding the texture.
        """
    def deleteAppearance(self, appearanceReference: int) -> None:
        """Deletes the appearance with the 'appearanceReference' index.

        Throws an exception if the current shared object is not of appearance type.

        Args:
            appearanceReference (int): The unique appearance reference 'key'.

        Raises:
            FMEException: If there is an error deleting the appearance.
        """
    def deleteGeometryDefinition(self, geometryDefinitionReference: int) -> None:
        """Deletes the geometry definition with the 'geometryDefinitionReference' index.

        Throws an exception if the current shared object is not of geometry definition type.

        Args:
            geometryDefinitionReference (int): The unique geometry definition reference 'key'.

        Raises:
            FMEException: If there is an error deleting the geometry definition.
        """
    def deleteTexture(self, textureReference: int) -> None:
        """Deletes the texture with the 'textureReference' index.

        Throws an exception if the current shared object is not of texture type.

        Args:
            textureReference (int): The unique texture reference 'key'.

        Raises:
            FMEException: If there is an error deleting the texture.
        """
    def getAppearanceCopy(self, appearanceReference: int) -> FMEAppearance or None:
        """This routine returns a copy of the referenced Appearance object from the Library.

        If there is no such Appearance in the Library, None is returned.

        Args:
            appearanceReference (int): The unique appearance reference.

        Returns:
            FMEAppearance: The copy of the appearance.
        """
    def getGeometryDefinitionCopy(
        self, geometryDefinitionReference: int
    ) -> FMEGeometry or None:
        """This routine returns a copy of the referenced Geometry Definition object from the Library.

        If there is no such Geometry Definition in the Library, None is returned.

        Args:
            geometryDefinitionReference (int): The unique geometry definition reference.

        Returns:
            FMEGeometry: The copy of the geometry definition.
        """
    def getTextureCopy(self, textureReference: int) -> FMETexture or None:
        """This routine returns a copy of the referenced Texture object from the Library.

        If there is no such Texture in the Library, None is returned.

        Args:
            textureReference (int): The unique texture reference.

        Returns:
            FMETexture: The copy of the texture.
        """
    def hasEntry(self, reference: int) -> bool:
        """This routine returns True if the Library has an entry with the 'reference' index.

        Args:
            reference (int): The unique reference.

        Returns:
            bool: True if the library has an entry with the reference.
        """
    def hasType(self, reference: int) -> int:
        """Returns the Library Type if library has an object with the specified reference number.

        Throws an exception if the supplied reference refers to an object without
        a valid object type, or if there is no object within the Library with the
        supplied reference number. Use hasEntry() to determine if the library
        contains the specified reference.

        Args:
            reference (int): The reference to search the library for.

        Returns:
            int: If the library has an object with the specified reference number
                the Library Type (FME_LIB_APPEARANCE, FME_LIB_TEXTURE, FME_LIB_RASTER,
                or FME_LIB_GEOMETRY_DEFINITION) is returned, otherwise an exception
                is thrown.

        Raises:
            FMEException: If there is an error determining the Library Type.
        """
    def replaceAppearance(
        self, appearanceReference: int, newAppearance: FMEAppearance
    ) -> None:
        """Replaces the Appearance with a new one at index = 'appearanceReference'.

        A FMEException is thrown if 'newAppearance' is None, 'appearanceReference'
        is not a valid index ,or the existing shared object is not an appearance type.
        If the 'newAppearance' successfully replaces the existing appearance, the
        library consumes the 'newAppearance'.

        Args:
            appearanceReference (int): The unique appearance reference 'key'.
            newAppearance (FMEAppearance): The new appearance.

        Raises:
            FMEException: If there is an error replacing the appearance.
        """
    def replaceGeometryDefinition(
        self, geometryDefinitionReference: int, newGeometryDefinition: FMEGeometry
    ) -> None:
        """Replaces the Geometry Definition with a new one at index = 'geometryDefinitionReference'.

        A FMEException is thrown if 'newGeometryDefinition' is None, 'geometryDefinitionReference'
        is not a valid index ,or the existing shared object is not a geometry definition type.
        If the 'newGeometryDefinition' successfully replaces the existing geometry definition, the
        library consumes the 'newGeometryDefinition'.

        Args:
            geometryDefinitionReference (int): The unique geometry definition reference 'key'.
            newGeometryDefinition (FMEGeometry): The new geometry definition.

        Raises:
            FMEException: If there is an error replacing the geometry definition.
        """
    def replaceTexture(self, textureReference: int, newTexture: FMETexture) -> None:
        """Replaces the Texture with a new one at index = 'textureReference'.

        A FMEException is thrown if 'newTexture' is None, 'textureReference'
        is not a valid index ,or the existing shared object is not a texture type.
        If the 'newTexture' successfully replaces the existing texture, the
        library consumes the 'newTexture'.

        Args:
            textureReference (int): The unique texture reference 'key'.
            newTexture (FMETexture): The new texture.

        Raises:
            FMEException: If there is an error replacing the texture.
        """

class FMEAppearance:
    """FME Appearance Class"""

    def __init__(self) -> None:
        """Create an instance of a blank appearance object"""
    def getAlpha(self) -> float or None:
        """This routine retrieves the alpha (1-transparency) of this Appearance.

        This will return None if it did not have a alpha associated with it.

        Returns:
            float: The alpha value
        """
    def getColorAmbient(self) -> tuple[float, float, float] or None:
        """This routine retrieves the ambient color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have an ambient color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the ambient color.
        """
    def getColorDiffuse(self) -> tuple[float, float, float] or None:
        """This routine retrieves the diffuse color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have a diffuse color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the diffuse color.
        """
    def getColorEmissive(self) -> tuple[float, float, float] or None:
        """This routine retrieves the emissive color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have an emissive color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the emissive color.
        """
    def getColorSpecular(self) -> tuple[float, float, float] or None:
        """This routine retrieves the specular color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have a specular color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the specular color.
        """
    def getMapperReference(self, mapperType: int) -> int or None:
        """This routine retrieves the texture reference of 'mapperType' of this Appearance.

        This will return None if it did not have a mapper of mapper type associated
        with it.

        Args:
            mapperType: The mapper type to retrieve the reference for. One of:
                FME_MAPPER_ALPHA_MAP, FME_MAPPER_ALPHA_MASK, FME_MAPPER_AMBIENT_MAP,
                FME_MAPPER_AMBIENT_MASK, FME_MAPPER_DIFFUSE_MAP, FME_MAPPER_DIFFUSE_MASK,
                FME_MAPPER_EMISSIVE_MAP, FME_MAPPER_EMISSIVE_MASK,
                FME_MAPPER_SHININESS_MAP, FME_MAPPER_SHININESS_MASK,
                FME_MAPPER_SPECULAR_MAP, FME_MAPPER_SPECULAR_MASK, FME_MAPPER_BUMP_MAP,
                OR FME_MAPPER_BUMP_MASK.

        Returns:
            int: The texture reference of 'mapperType' of this Appearance.
        """
    def getName(self) -> text_type or None:
        """This routine retrieves the 'name' of this Appearance as a six.text_type. This will return None if it did not have a name associated with it.

        Returns:
            str: The name of this Appearance.
        """
    def getShininess(self) -> float or None:
        """This routine retrieves the shininess of this Appearance.

        This will return None if it did not have a shininess associated with it.

        Returns:
            float: The shininess of this Appearance.
        """
    def getTextureReference(self) -> int or None:
        """This routine retrieves the main texture reference of this Appearance.

        This will return None if it did not have a texture reference associated with it.

        Returns:
            int: The texture reference of this Appearance.
        """
    def removeMapperReference(self, mapperType: int) -> None:
        """Remove the specified mapper reference form this appearance

        Args:
          The mapper reference to remove.
        """
    def removeTextureReference(self) -> None:
        """Remove the texture reference form this appearance"""
    def setAlpha(self, alpha: float) -> None:
        """This routine sets the alpha of this Appearance.

        The alpha should be a floating point value in the range of 0.0 to 1.0,
        where 0.0 represents a fully transparent color, and 1.0 represents a
        fully opaque color. Setting the value to negative will remove this
        property from this appearance.

        Args:
            alpha (float): The alpha value to set.
        """
    def setColorAmbient(self, r: float, g: float, b: float) -> None:
        """This routine sets the ambient color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setColorDiffuse(self, r: float, g: float, b: float) -> None:
        """This routine sets the diffuse color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setColorEmissive(self, r: float, g: float, b: float) -> None:
        """This routine sets the emissive color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setColorSpecular(self, r: float, g: float, b: float) -> None:
        """This routine sets the specular color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setMapperReference(self, mapperType: int, textureReference: int) -> bool:
        """This routine sets a Mapper that modifies this Appearance.

        The Mapper is a texture object that modifies some property of the Appearance.
        One of: FME_MAPPER_ALPHA_MAP, FME_MAPPER_ALPHA_MASK, FME_MAPPER_AMBIENT_MAP,
        FME_MAPPER_AMBIENT_MASK, FME_MAPPER_DIFFUSE_MAP, FME_MAPPER_DIFFUSE_MASK,
        FME_MAPPER_EMISSIVE_MAP, FME_MAPPER_EMISSIVE_MASK, FME_MAPPER_SHININESS_MAP,
        FME_MAPPER_SHININESS_MASK, FME_MAPPER_SPECULAR_MAP, FME_MAPPER_SPECULAR_MASK,
        FME_MAPPER_BUMP_MAP, OR FME_MAPPER_BUMP_MASK. The 'textureReference' should
        refer to a Texture found in the common FMELibrary. True will be returned
        if the reference supplied refers to a valid Texture in the library, False
        indicates a hanging reference.

        Args:
            mapperType: The mapper type to set the reference for.
            textureReference: The texture reference to set.

        Returns:
            bool: Returns True if the reference supplied refers to a valid texture
                in the library and False otherwise.
        """
    def setName(self, name: text_type) -> None:
        """This routine sets the 'name' of this Appearance with a six.text_type .

        (It need not be a unique name among other, possibly different Appearances.)
        Setting the 'name' to be (blank) will remove the name from this Appearance.

        Args:
            name (text_type): The name to set.
        """
    def setShininess(self, shininess: float) -> None:
        """This routine sets the shininess of this Appearance.

        The shininess should be a floating point value in the range of 0.0 to 1.0,
        where 0.0 represents a fully dull material, and 1.0 represents a fully shiny
        material. Setting the value to negative will remove this property from this
        appearance.

        Args:
            shininess (float): The shininess to set.
        """
    def setTextureReference(self, textureReference: int) -> bool:
        """This routine sets the main texture reference of this Appearance.

        The texture reference should be valid reference to a Texture found in the
        common FMELibrary. True will be returned if the reference supplied refers
        to a valid Texture in the library, false indicates a hanging reference.

        Args:
            textureReference (int): The texture reference to set.

        Returns:
            bool: Returns True if the reference supplied refers to a valid texture
                in the library and False otherwise.
        """

FME_LEFT_HAND_RULE: int
FME_RIGHT_HAND_RULE: int

class FMESimpleAreaIterator:
    """FME Simple Area Iterator Class

    FMESimpleAreaIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEDonut to get an FMESimpleAreaIterator which can be
    used to iterate over its geometries."""

class FMEAreaIterator:
    """FME Area Iterator Class

    FMEAreaIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMultiArea to get an FMEAreaIterator which can be
    used to iterate over its geometries."""

class FMEArea(FMEGeometry):
    """FME Area Class

    FMEArea is an abstract class. It cannot be created directly.
    """

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool:
        """Returns True if the outer boundary (and inner boundaries in the case
        of FMEDonut) of this area contains FMELine only.

        Returns:
            (bool): Whether the area's boundaries contain only lines.
        """
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool:

        """Determines if area is convex.

        The polygon making up the area is convex if all internal angles are less
        than 180 degrees and it's not self-intersecting. Imperfectly planar 3D
        polygons are tolerated.

        Returns:
            (bool): Whether the area is convex.
        """
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane (if plane equation D is specified - see below).

        If given normal is the zero vector, the normal used to check the planarity
        is computed using Newell's method as in isPlanar(). valD is a reference
        to a value of D in the plane equation AX + BY + CZ = D. It can be used to
        make sure that multiple pieces lie in the same plane. If 'recalculateD'
        is set to False, the passed in value of D will be used in the calculation.
        If 'recalcualteD' is set to True, the passed in value is ignored and is
        instead automatically calculated (and returned in the second position of
        the returned tuple). A useful calling pattern for ensuring co-planarity
        is to get valD computed on the first call to the function setting
        recalculateD to True, and then use this value for future calls with
        recalculateD to False.

        Args:
            tolerance (float): The tolerance to check against.
            normalVector (tuple[float, float, float]): The normal used to check the planarity.
            valD (float): The value D from 'AX + BY + CZ = D'.
            recalculateD (bool): Whether to recalculate 'D' or not.

        Returns:
            (bool, tuple[float, float, float], float): A tuple containing a
                boolean, tuple, and float representing:
                1) Whether or not the area is in plane;
                2) The normal vector returned; and
                3) The value 'D'.
                Note: If recalculateD is False, the tuple returned will only
                contain the boolean and vector tuple (i.e. 'valD' is not returned).
        """
    def isOriented(self, rightOrLeft: int) -> bool:
        """This returns True if the geometry has the specified orientation.

        Args:
          rightOrLeft (int):The orientation to check the FMEArea for.

        Returns:
          (bool): Whether the area has the specified orientation.
        """
    def isPlanar(self, tolerance: float) -> bool:
        """Returns True if this is planar within the given tolerance, and False otherwise.

        The planarity condition is computed by the following algorithm. The
        normal vector <A, B, C> is determined by the vertices of this area using
        Newell's method. For the first point (x', y', z') of this area, we
        compute D' = Ax' + By' + Cz'. Then, this area is planar if and only if
        every subsequent point (x, y, z) of this area gives a D = Ax + By + Cz,
        that is within the tolerance amount of D'. That is, | D - D' | <= tolerance.

        If the specified tolerance is negative, then this method always returns True.

        Args:
            tolerance (float): The tolerance to check against.

        Returns:
            (bool): Whether the area is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the area by the coords specified by 'offsetPoint'.

        Raises:
            FMEException: An exception is raised if an error occurred
        """
    def orient(self, rightOrLeft: int) -> None:
        """Orients the area to the specified right or left.

        Args:
          rightOrLeft (int): The orientation to set on the FMEArea.
        """
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise
        only x and y are.

        Args:
          checkZ (bool): Whether to check Z values.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None:
        """This reverses the order of the area's points."""
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """Rotate the area counterclockwise around the 'center' point by the
        specified 'angle' (in degrees).

        Args:
          centre (FMEPoint): The centre of rotation.
          angle (float): The angle to rotate by.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the area by the specified x, y, and z scales.

        Args:
          xScale (float): The x scale factor.
          yScale (float): The y scale factor.
          zScale (float): The z scale factor.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEMultiArea(FMEGeometry):
    """FME MultiArea class."""

    @overload
    def __init__(self) -> None:
        """Default FMEMultiArea constructor.

        Returns:
          (FMEMultiArea): An instance of a MultiArea geometry object.
        """
    @overload
    def __init__(self, multiArea: FMEMultiArea) -> None:
        """Create a copy of the passed in Multi-Area geometry object..

        Args:
          multiArea (FMEMultiArea): An instance of a MultiArea geometry object.

        Returns:
          (FMEMultiArea): An instance of a MultiArea geometry object.
        """
    def appendPart(self, area: FMEArea) -> None:
        """This appends the area to the MultiArea.

        If None is passed in, nothing will be appended. All areas in the MultiArea
        will be forced to have the same dimension. If any 3D areas exist, all 2D
        areas will be converted to 3D with a default Z value of 0.0.

        Args:
          area (FMEArea): The area to append to the MultiArea.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getPartAt(self, index: int) -> FMEArea or None:
        """Returns the area at the specified index.

        Args:
          index (int): The index of the area to return.

        Returns:
          (FMEArea): The area at the given index. Note: This method returns a
              terminal area type of the FMEArea; i.e. one of the leaf classes in
              the FMEArea inheritance graph. For example, a FMEPolygon is returned
              if the area truly is a polygon.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane (if plane equation D is specified - see below).

        If given normal is the zero vector, the normal used to check the planarity
        is computed using Newell's method as in isPlanar(). valD is a reference
        to a value of D in the plane equation AX + BY + CZ = D. It can be used to
        make sure that multiple pieces lie in the same plane. If 'recalculateD'
        is set to False, the passed in value of D will be used in the calculation.
        If 'recalcualteD' is set to True, the passed in value is ignored and is
        instead automatically calculated (and returned in the second position of
        the returned tuple). A useful calling pattern for ensuring co-planarity
        is to get valD computed on the first call to the function setting
        recalculateD to True, and then use this value for future calls with
        recalculateD to False.

        Args:
          tolerance (float): The tolerance to check against.
          normalVector (tuple[float]): The normal used to check the planarity.
          valD (float): The value of D in the plane equation AX + BY + CZ = D.
          recalculateD (bool): Whether to recalculate D.

        Returns:
          (bool, tuple[float], float): A tuple containing the following:
            - (bool): True if the area is in plane.
            - (tuple[float, float, float]): The normal vector of the plane.
            - (float): The value of D in the plane equation AX + BY + CZ = D.
        """
    def isPlanar(self, tolerance: float) -> bool:
        """Returns True if this is planar within the given tolerance, and False otherwise.

        The planarity condition is computed by the following algorithm. The normal
        vector <A, B, C> is determined by the vertices of this area using Newell's
        method. For the first point (x', y', z') of this area, we
        compute D' = Ax' + By' + Cz'. Then, this area is planar if and only if
        every subsequent point (x, y, z) of this area gives a D = Ax + By + Cz,
        that is within the tolerance amount of D'. That is, | D - D' | <= tolerance.

        Args:
          tolerance (float): The tolerance to check against.

        Returns:
          (bool): Whether the multiarea is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """This returns the number of areas that make up this MultiArea.

        Returns:
          (int): The number of parts in this MultiArea.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """This offsets the MultiArea by the specified point.

        Args:
          offsetPoint (FMEPoint): The point to offset the MultiArea by.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def removeLastPart(self) -> FMEArea or None:
        """This removes and returns the last area of the MultiArea.

        If there are no areas in the MultiArea, it will return None.

        Returns:
          (FMEArea): The last area of the MultiArea. Note: This method returns a
          terminal area type of the FMEArea; i.e. one of the leaf classes in the
          FMEArea inheritance graph. For example, a FMEPolygon is returned if the
          area truly is a polygon.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates the MultiArea about the specified point by the specified angle.

        Args:
          center (FMEPoint): The point to rotate about.
          angle (float): The angle to rotate by.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the MultiArea by the specified factors.

        Args:
          xScale (float): The x-scale factor.
          yScale (float): The y-scale factor.
          zScale (float): The z-scale factor.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEDonut(FMEArea):
    """FME Donut Class"""

    @overload
    def __init__(self, outerBoundary: FMESimpleArea) -> None:
        """Creates a new Donut geometry object.

        The simple area passed in is used to define the outer boundary of the donut.

        Args:
          outerBoundary (FMESimpleArea): The simple area defining the outer boundary of the donut.

        Returns:
          (FMEDonut): The newly created Donut geometry object.
        """
    @overload
    def __init__(self, outerBoundary: FMECurve) -> None:
        """Creates a new Donut geometry object.

        The curve passed in is used to define the outer boundary of the donut.

        Args:
          outerBoundary (FMECurve): The outer boundary as a curve.

        Returns:
          (FMEDonut): The newly created Donut geometry object.
        """
    @overload
    def __init__(self, donut: FMEDonut) -> None:
        """Create a copy of the passed in Donut geometry object.

        Args:
          donut (FMEDonut): The Donut geometry object to create a copy of.

        Returns:
          (FMEDonut): The newly created Donut geometry object.
        """
    def addInnerBoundaryCurve(self, innerBoundary: FMECurve) -> None:
        """If the inner boundary being added has a different dimension than the
        other boundaries, anything 2D will be forced to 3D.

        Note that the default Z value is 0.0 when forcing 2D geometry to 3D. If
        the curve is not closed, the closure will be assumed as a straight line
        from the start point to the end point. If the 'innerBoundary' being added
        is None, nothing will be done.

        Args:
          innerBoundary (FMECurve): The curve defining the inner boundary.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def addInnerBoundarySimpleArea(self, innerBoundary: FMESimpleArea) -> None:
        """Adds a simple area as an inner boundary.

        If the inner boundary being added has a different dimension than the other
        boundaries, anything 2D will be forced to 3D. Note that the default Z value
        is 0.0 when forcing 2D geometry to 3D. If the 'innerBoundary' being added
        is None, nothing will be done.

        Args:
          innerBoundary (FMESimpleArea): The simple area defining the inner boundary.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getInnerBoundaryAsCurveAt(
        self, index: int
    ) -> FMEPath or FMEArc or FMELine or None:
        """Retrieves the inner boundary at the specified index.

        If the index is out of bounds, it will return None.

        Args:
          index (int): The index of the inner boundary to retrieve.

        Returns:
          (FMEPath or FMEArc or FMELine or None): The inner boundary as a FMECurve,
          or None if the specified index is greater than the number of inner
          boundaries. Returns the terminal geometry of the FMECurve, either a
          FMEPath, FMEArc or FMELine.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getInnerBoundarAsSimpleAreaAt(
        self, index: int
    ) -> FMEPolygon or FMEEllipse or None:
        """Retrieves the inner boundary at 'index' as a FMESimpleArea.

        Args:
          index (int): The index of the inner boundary to retrieve.

        Returns:
          (FMESimpleArea or None):The inner boundary as a FMESimpleArea, or None
          if the specified index is greater than the number of inner boundaries.
          Returns the terminal geometry of the FMESimpleArea, either a FMEPolygon
          or a FMEEllipse.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getOuterBoundaryAsCurve(self) -> FMEPath or FMEArc or FMELine:
        """Retrieves the outer boundary as a FMECurve.

        Returns:
          (FMEPath, FMEArc or FMELine): The inner boundary as a FMECurve. Returns
              the terminal geometry of the FMECurve, either a FMEPath, FMEArc or
              FMELine.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getOuterBoundaryAsSimpleArea(self) -> FMEPolygon or FMEEllipse:
        """Retrieves the outer boundary as a FMESimpleArea.

        Returns:
          (FMEPolygon or FMEEllipse): The outer boundary as a FMESimpleArea.
              Returns the terminal geometry of the FMESimpleArea, either a
              FMEPolygon or a FMEEllipse.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numInnerBoundaries(self) -> int:
        """Returns the number of inner boundaries.

        Returns:
          (int): The number of inner boundaries.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeLastInnerBoundaryAsCurve(self) -> FMEPath or FMEArc or FMELine:
        """Removes and returns the last inner boundary as a FMECurve.

        Returns:
          (FMEPath, FMEArc or FMELine): The last inner boundary as a FMESimpleArea.
              Returns the terminal geometry of the FMESimpleArea, either a
              FMEEllipse, or FMEPolygon.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setOuterBoundaryCurve(self, outerBoundary: FMECurve) -> None:
        """Sets the outer boundary as a FMECurve.

        If the curve is not closed, the closure will be assumed as a straight line
        from the start point to the end point. If the new outer boundary has a
        different dimension than the inner boundaries, everything will be forced
        to 3D. Note that the default Z value is 0.0 when forcing 2D geometry to
        3D. This will return an error if the outerBoundary passed in is invalid
        or None.

        Args:
          outerBoundary (FMECurve): The curve to set as the outer boundary.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setOuterBoundarySimpleArea(self, outerBoundary: FMESimpleArea) -> None:
        """Sets the outer boundary as a FMESimpleArea.

        Sets the outer boundary of the donut. If the new outer boundary has a
        different dimension than the inner boundaries, everything will be forced
        to 3D. Note that the default Z value is 0.0 when forcing 2D geometry to 3D.

        Args:
          outerBoundary (FMESimpleArea): The simple area to set as the outer
              boundary.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMESimpleArea(FMEArea):
    """FME Simple Area Clas

    FMESimpleArea is an abstract class. It cannot be created directly."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getBoundaryAsCurve(self) -> FMEPath or FMEArc or FMELine:
        """Returns the curve that defines the boundary of the area.

        Returns:
          (FMEPath, FMEArc or FMELine): Returns the curve that defines the
              boundary of the area.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEEllipse(FMESimpleArea):
    """FME Ellipse Class"""

    @overload
    def __init__(self, boundary: FMEArc) -> None:
        """This routine creates a new Ellipse geometry object from the passed in arc boundary.

        If this arc is not closed, the closure will be assumed as a complete
        continuation of the arc where the end point is 360 degrees from the the
        start point.

        Args:
          boundary (FMEArc): The boundary as an arc.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    @overload
    def __init__(
        self,
        centerPoint: FMEPoint,
        primaryRadius: float,
        secondaryRadius: float,
        rotation: float,
        orientation: int,
    ) -> None:
        """This routine creates a new Ellipse geometry object using the passed in values.

        Args:
          centerPoint (FMEPoint): The center point of the ellipse.
          primaryRadius (float): The primary radius of the ellipse.
          secondaryRadius (float): The secondary radius of the ellipse.
          rotation (float): The rotation of the ellipse.
          orientation (int): The orientation rule. Must be either
              FME_RIGHT_HAND_RULE or FME_LEFT_HAND_RULE.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    @overload
    def __init__(self, ellipse: FMEEllipse) -> None:
        """This routine creates a new Ellipse geometry object from the passed in ellipse.

        Args:
          ellipse (FMEEllipse): The ellipse to copy.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.
        """
    @overload
    def __init__(self) -> None:
        """This routine creates a new Ellipse geometry object.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getAsLine(self) -> FMELine or None:
        """Returns the ellipse as a line.

        Returns:
          (FMELine): The line representing the ellipse or None if the ellipse
              cannot be returned as a line.
        """
    def getBoundaryAsArc(self) -> FMEArc or None:
        """Returns the ellipse as an arc.

        Returns:
          (FMEArc): The arc representing the ellipse or None if the ellipse
              cannot be returned as an arc.
        """
    def getBoundaryAsCurve(self) -> FMEPath or FMEArc or FMELine:
        """Returns the ellipse as a curve.

        Returns:
          (FMEPath or FMEArc or FMELine): The curve representing the ellipse.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getPrimaryRadius(self) -> float:
        """This gets the primary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Returns:
          (float): The primary radius of the ellipse.
        """
    def getRotation(self) -> float:
        """This gets the rotation of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Returns:
          (float): The rotation of the ellipse.
        """
    def getSecondaryRadius(self) -> float:
        """This gets the secondary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Returns:
          (float): The secondary radius of the ellipse.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setBoundary(self, boundary: FMEArc) -> None:
        """This sets the curve that defines the boundary of the ellipse.

        If this arc is not closed, the closure will be assumed as a complete
        continuation of the arc where the end point is 360 degrees from the the
        start point. If an error occurs, an exception is thrown.

        Args:
          boundary (FMEArc): The new boundary of the ellipse.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setPrimaryRadius(self, radius: float) -> None:
        """This sets the primary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Args:
          radius (float): The new primary radius of the ellipse.
        """
    def setSecondaryRadius(self, radius: float) -> None:
        """This sets the secondary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Args:
          radius (float): The new secondary radius of the ellipse.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEPolygon(FMESimpleArea):
    """FME Polygon Class"""

    @overload
    def __init__(self, boundary: FMECurve) -> None:
        """Create an instance of a Polygon geometry object.

        The curve passed in, 'boundary', is used to define the boundary of the polygon.

        Args:
          boundary (FMECurve): The boundary as a curve.

        Returns:
          (FMEPolygon): The new polygon.
        """
    @overload
    def __init__(self, polygon: FMEPolygon) -> None:
        """Create a copy of the passed in Polygon geometry object.

        Args:
          polygon (FMEPolygon): The polygon.

        Returns:
          (FMEPolygon): The new polygon.
        """
    @overload
    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getBoundaryAsCurve(self) -> FMEPath or FMEArc or FMELine: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setBoundary(self, boundary: FMECurve) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

# No Coordinate Index
FME_NPOS32: int

# Snip Types
SNIP_DISTANCE: int
SNIP_PERCENTAGE: int
SNIP_VERTEX: int
SNIP_POINT: int

# Arc Types
FME_ARC_BY_CENTER_POINT: int
FME_ARC_BY_CENTER_POINT_START_END: int
FME_ARC_BY_BULGE: int
FME_ARC_BY_3_POINTS: int

# Mapping File Directives
kFMEStrokeMaxDeviationValue: int
kFMEDegreesPerEdge: int

class FMECurve(FMEGeometry, TransformMixin):
    """FME Curve Class

    FMECurve is an abstract class. It cannot be created directly."""

    def getAsLine(self) -> FMELine:
        """Returns the curve as a line geometry object.

        Returns:
            FMELine: A line geometry object.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            FMELine: The curve as a FMELine object.
        """
    def getEndPoint(self) -> FMEPoint or None:
        """Returns the end point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The end point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the curve.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            float: The length of the curve.
        """
    def getStartPoint(self) -> FMEPoint or None:
        """Returns the start point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The start point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            bool: True if the curve contains only lines, False otherwise.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise only
        x and y are.

        Args:
            checkZ (bool): Whether to check the Z coordinate of the points.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions.

        Either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index; and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location.
            endLocation (float): The end location.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same, keep
        two same points.

        Args:
            startPoint (FMEPoint): The start point.
            endPoint (FMEPoint): The end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEMultiCurve(FMEGeometry):
    """FME Multi-Curve Class"""

    def __init__(self, multiCurve: FMEMultiCurve) -> None:
        """Initializes a new instance of the FMEMultiCurve class.

        Args:
            multiCurve (FMEMultiCurve): The multi-curve to copy.

        Returns:
            An instance of the FMEMultiCurve class.
        """
    def appendPart(self, curve: FMECurve) -> None:
        """This appends the curve to the MultiCurve.

        If None is passed in, nothing will be appended. All curves in the
        MultiCurve will be forced to have the same dimension. If any 3D curves
        exist, all 2D curves will be converted to 3D with a default Z value of 0.0.

        Args:
            curve (FMECurve): The curve to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendParts(self, multiCurve: FMEMultiCurve) -> None:
        """This appends the MultiCurve passed in to the existing MultiCurve.

        If None is passed in, nothing will be appended.

        Args:
            multiCurve (FMEMultiCurve): The multi-curve to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPartAt(self, index: int) -> FMECurve or None:
        """Returns the curve at the specified index.

        Args:
            index (int): The index of the curve to return.

        Returns:
            FMECurve: The curve at the given index. Note: This method returns a
            terminal curve type of the FMECurve; i.e. one of the leaf classes in
            the FMECurve inheritance graph. For example, a FMELine is returned
            if the curve truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def numParts(self) -> int:
        """Returns the number of parts in the MultiCurve.

        Returns:
            int: The number of parts in the MultiCurve.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offset this geometry by the given offset point.

        Args:
            offsetPoint (FMEPoint): The point to offset the coordinates of the geometry by.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeLastPart(self) -> FMECurve or None:
        """This removes and returns the last curve of the MultiCurve.

        If there are no curves in the MultiCurve, it will return None.

        Returns:
            FMECurve: The last curve of the MultiCurve. Note: This method returns
                a terminal curve type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMELine
                is returned if the curve truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scale the curve by the given scaling factors.

        Args:
            xScale (float): The X scaling factor.
            yScale (float): The Y scaling factor.
            zScale (float): The Z scaling factor.
        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEPath(FMECurve, TransformMixin):
    """FME Path Class"""

    def __init__(self, path: FMEPath) -> None:
        """Initializes a new instance of the FMEPath class.

        Args:
            path (FMEPath): The path to copy.

        Returns:
            An instance of the FMEPath class.
        """
    def appendPart(self, curve: FMECurve) -> None:
        """Append an entire curve.

        If the path and the curve are not connected, a new line will be inserted
        between them. If any 3D segments exist, all 2D segments will be converted
        to 3D with a default Z value of 0.0.

        Args:
            curve (FMECurve): The curve to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendPartWithSnapping(self, curve: FMECurve) -> None:
        """Append an entire segment.

        If the path and the curve are not connected, the first point on the
        curve will be moved to instead be the last point on the path.
        If any 3D segments exist, all 2D segments will be converted to 3D with a
        default Z value of 0.0.

        Args:
            curve (FMECurve): The curve to append with snapping.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPoint(self, point: FMEPoint) -> None:
        """Extend the path to the given point.

        If the point is 2D and the path is 3D, the point will be set to 3D with
        a Z value of 0.0. If the path is 2D and the point is 3D, the segments in
        the path will be set to 3D with 0.0 for Z values. If None is passed in,
        nothing will be appended.

        Args:
            point (FMEPoint): The point to be extended to.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointXY(self, xcoord: float, ycoord: float) -> None:
        """Extend the path to the given point.

        If this method is called on a 3D line, a Z value of 0.0 will be used for
        each appended point.

        Args:
            xcoord (float): The X coordinate of the point.
            ycoord (float): The Y coordinate of the point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointXYZ(self, xcoord: float, ycoord: float, zcoord: float) -> None:
        """Extend the path to the given point.

         If this method is called on a 2D line, the line will be forced to 3D
         with a default Z value of 0.0.

        Args:
            xcoord (float): The X coordinate of the point.
            ycoord (float): The Y coordinate of the point.
            zcoord (float): The Z coordinate of the point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointsXY(self, coords: list[tuple[float]]) -> None:
        """Extend the path to a list of points.

        If this method is called on a 3D path, a Z value of 0.0 will be used for
        each appended point.

        Args:
            coords (list[tuple[float]]): The list of 2D points to be extended to.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointsXYZ(self, coords: list[tuple[float]]) -> None:
        """Extend the path to a list of points.

        If this method is called on a 2D path, the path will be forced to 3D with
        a default Z value of 0.0.

        Args:
            coords (list[tuple[float]]): The list of 3D points to be extended to.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAsLine(self) -> FMELine:
        """Returns the path as a line.

        Returns:
            FMELine: The path as a line.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which denotes
        the maximum deviation of the arc from the line. In the absence of this
        directive or the value of this directive is smaller than or equal to 0,
        the number points will be determined by the arc's sweep angle and the
        value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            FMELine: The path as a as a FMELine object.
        """
    def getEndPoint(self) -> FMEPoint or None:
        """Returns the end point of the path.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The end point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the path.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            float: The length of the path.
        """
    def getPartAt(self, index: int) -> FMEArc or FMELine:
        """This returns the part of the FMEPath at the given index.

        This returns None if the index is out of range.

        Args:
            index (int): The index of the part to return.

        Returns:
            FMEArc or FMELine: The FMESegment at the given index. Returns the
                terminal geometry of the FMESegment, either a FMEArc or FMELine.
        """
    def getStartPoint(self) -> FMEPoint or None:
        """Returns the start point of the path.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The start point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.

        If 'threeD' is True, the z coordinate of the start and end points will be
        compared. This does not take measures into consideration.

        Args:
            threeD (bool): Whether to compare the z coordinate value.

        Returns:
            bool: True if the start and end point have identical coordinate
                values, False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            bool: True if the curve contains only lines, False otherwise.
        """
    def numParts(self) -> int:
        """This returns the number of FMESegment that make up this path.

        Returns:
            int: The number of FMESegment that are used to make the FMEPath.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None:
        """Remove duplicate points from the path.

        If 'checkZ' is True, the z coordinate of the points will be compared.

        Args:
            checkZ (bool): Whether to compare the z coordinate value.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeEndPart(self) -> FMEArc or FMELine:
        """This removes the end FMESegment of the path.

        If there are no segments in the FMEPath, None is returned.

        Returns:
            FMEArc or FMELine: The end FMESegment of the path, or None if there
                are no segments in the FMEPath.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The end point to set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point to set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions.

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location to snip at.
            endLocation (float): The end location to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same, keep
        two same points.

        Args:
            startPoint (FMEPoint): The start point to snip at.
            endPoint (FMEPoint): The end point to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMESegment(FMECurve):
    """FME Segment Class

    FMESegment is an abstract class. It cannot be created directly."""

    def getAsLine(self) -> FMELine:
        """Returns the segment as a line.

        Returns:
            FMELine: The segment as a line.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            FMELine: The segment as a line.
        """
    def getEndPoint(self) -> FMEPoint or None:
        """Returns the end point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint or None: The end point of the segment.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of this curve.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            float: The length of the segment.
        """
    def getStartPoint(self) -> FMEPoint or None:
        """Returns the start point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint or None: The start point of the segment.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.

        If 'threeD' is True, the z coordinate of the start and end points will be
        compared. This does not take measures into consideration.

        Args:
            threeD (bool): Whether to compare the z coordinate value.

        Returns:
            bool: True if the start and end point have identical coordinate
                values, False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            bool: True if the curve contains only lines, False otherwise.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise
        only x and y are.

        Args:
            checkZ (bool): Whether to check the z coordinate value.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The point to set at the end of the curve.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The point to set at the start of the curve.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location to snip at.
            endLocation (float): The end location to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same, keep
        two same points.

        Args:
            startPoint (FMEPoint): The start point to snip at.
            endPoint (FMEPoint): The end point to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMESegmentIterator:
    """FME SegmentIterator Class"""

class FMELine(FMESegment):
    """FME Line Class"""

    @overload
    def __init__(self, is3D: bool) -> None:
        """Constructs a 3D line if 'is3D' is True, otherwise a 2D line is created.

        Args:
            is3D (bool): The value to set the line’s dimension.

        Returns:
            An instance of a Line Geometry object
        """
    @overload
    def __init__(self, points: list[tuple[float]]) -> None:
        """Constructs a line from a list of points.

        Args:
            points (list[tuple[float]]): The list of points to set to the line.
                The points are represented as (x, y) or (x, y, z) tuples

        Returns:
            An instance of a Line Geometry object
        """
    @overload
    def __init__(self, line: FMELine) -> None:
        """Constructs a line from another line.

        Args:
            line (FMELine): The line to copy

        Returns:
            An instance of a Line Geometry object
        """
    def appendLine(self, line: FMELine) -> None:
        """Appends 'line' to the end of the existing line.

        If the existing line has no coordinates, it will have its geometry
        dimension set based on the first append call made. This line's points
        will be forced to have a consistent dimension. If a 2D line is appended
        to a 3D line, the 2D line will be changed to 3D with a Z value of 0.0.
        If a 3D line is appended to a 2D line, the 2D line will be changed to
        3D with 0.0 for all Z values. The appended line will be forced to have
        consistent measures. Any unspecified measure values will be set to None.

        Args:
            line (FMELine): The line to append
        """
    def appendPoint(self, point: FMEPoint or tuple[float, float, float]) -> None:
        """Appends 'point' to the end of the existing line.

        Lines with no coordinates will have their dimension set based on the
        first append call made. The line's points will be forced to have a
        consistent dimension. If a 2D point is appended to a 3D line, the point
        will be changed to 3D with a Z value of 0.0. If a 3D point is appended
        to a 2D line, the line will be changed to 3D with 0.0 for all Z values.
        The points will be forced to have consistent measures. Any unspecified
        measure values will be set to None. Nothing is appended if None is passed in.

        Args:
            point (FMEPoint or tuple): The point to append

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def appendPoints(self, points: list[FMEPoint]) -> None:
        """Appends 'points' to the end of the existing line.

        Lines with no coordinates will have their geometry dimension set based
        on the first append call made. If this method is called on a 3D line, a
        Z value of 0.0 will be used for each appended point. If this method is
        called on a 2D line, the line will be forced to 3D with a default Z value
        of 0.0. Because this method does not specify measure values, a value of
        None will be used for each point for any existing measures.

        Args:
            points (list[FMEPoint]): The list of points to append

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def getAsLine(self) -> FMELine:
        """Returns the curve as a line.

        Returns:
            (FMELine): The curve as a FMELine object.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            (FMELine): The curve as a FMELine object.
        """
    def getEndPoint(self) -> FMEPoint or None:
        """Returns the end point of the line.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint or None): The end point of the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the line.

        If 'threeD' is True, this returns the 3D length of the curve,
        otherwise this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            (float): The length of the line.
        """
    def getPointAt(self, index: int) -> FMEPoint:
        """Gets the point at the specified 'index'.

        An error is returned if the index is out of range.

        Args:
            index (int): The index of the point to return.

        Returns:
            (FMEPoint): The point at the given index.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPoints(self) -> list[FMEPoint]:
        """Gets the points of the line as a list of FMEPoint objects.

        An exception is raised if an error occurred getting a point from the line.

        Returns:
            (list[FMEPoint]): The points of the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getStartPoint(self) -> FMEPoint or None:
        """Returns the start point of the line.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint or None): The start point of the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def indexOfCoord(self, coord: tuple[float, float, float]) -> int:
        """Returns the index of the first coordinate defined within the tuple 'coord',
        or FME_NPOS32 if no such coordinate is found.

        Args:
            coord (tuple): The z tuple containing coordinate whose index to search.

        Returns:
            (int): The index of the supplied coordinate,
                or FME_NPOS32 if no such coordinate exists.
        """
    def insertPointAtIndex(self, point: FMEPoint, index: int) -> None:
        """Inserts a point at the specified 'index'.

        All points from that index on will be shifted to allow room for the new
        point. Any new measures added to the point will be set a default of None.

        Args:
            point (FMEPoint): The point to insert.
            index (int): The index of the point to remove.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.
        If 'threeD' is True, the z coordinate of the start and end points will
        be compared. This does not take measures into consideration.

        Args:
            threeD (bool): Whether to compare the z coordinate value.

        Returns:
            (bool): True if the start and end point have identical coordinate values, False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            (bool): True if the curve contains only lines, False otherwise.
        """
    def numPoints(self) -> int:
        """Returns the number of points in the line.

        Returns:
            (int): The number of points in the line.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the line by the distance from the start point to the supplied point.

        The offset point is the point from which the line will be offset.
        The offset point will be removed from the line.

        Args:
            offsetPoint (FMEPoint): The point from which the line will be offset.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes duplicate points from the line.

        If 'checkZ' is True, the z coordinate of the points will be compared.
        This does not take measures into consideration.

        Args:
            checkZ (bool): Whether to compare the z coordinate value.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removePointAt(self, index: int) -> FMEPoint or None:
        """Removes the point at the specified 'index' and returns.

        Null is returned if the index is out of range.

        Args:
            index (int): The index of the point to remove.

        Returns:
            (FMEPoint or None): The point removed, or None if the index is out of range.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def reset(self, coords: list[tuple[float, float, float]]) -> None:
        """Resets the coordinates to an 'empty' state.

        It does not alter the geometry dimension, but it does remove all measures.
        If 'coords' is supplied, then this method sets the line's coordinates to
        the values in the supplied 'coords' list. None zCoord values will result
        in a 2D line, otherwise a 3D line is created. This method removes all measures.

        Args:
            coords (list[tuple]): (Optional) The list of coordinate tuples to
                add after the reset.
        """
    def reverse(self) -> None:
        """Reverses the order of the points in the line."""
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """Rotate the curve counterclockwise around the 'center' point by the
        specified 'angle' (in degrees).

        The angle is specified in radians.

        Args:
            centre (FMEPoint): The centre of the rotation.
            angle (float): The angle of the rotation.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the line by the supplied 'xScale', 'yScale' and 'zScale'.

        Args:
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.
            zScale (float): (optional) The z scale factor.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setEndPoint(self, point: FMEPoint) -> None:
        """Sets the end point of the line.

        Args:
            point (FMEPoint): The point to set as the end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setPointAt(self, index: int, point: FMEPoint) -> None:
        """Sets 'point' at the specified index.

        The line's points will be forced to have a consistent dimension. If any
        points are 3D, they all must be. A Z value of 0.0 is used when converting
        from a 2D point to a 3D point. The points will be forced to have
        consistent measures. Any unspecified measure values will be set to None.
        An error is returned if the index is out of range.

        Args:
            index (int): The index of the point to set.
            point (FMEPoint): The point to set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Sets the start point of the line.

        Args:
            point (FMEPoint): The point to set as the start point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The location at which to split the line.
            endLocation (float): The location at which to split the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same,
        keep two same points.

        Args:
            startPoint (FMEPoint): The start point.
            endPoint (FMEPoint): The end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEArc(FMESegment):
    """FME Arc Class"""

    @overload
    def __init__(self, threePoints: tuple[FMEPoint, FMEPoint, FMEPoint]) -> None:
        """Creates an arc using the 3 points contained in the tuple.

        If 'startPoint' and 'endPoint' (threePoints[0] and threePoints[2]) and
        are equal, then the arc will be coincident with the circle whose center
        point is midway between startPoint and midpoint (threePoints[0] and threePoints[1]).

        Args:
            threePoints (tuple[FMEPoint]): The tuple containing 3 points to create
                the arc in the form (startPoint, midPoint, endPoint).

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(self, twoPoints: tuple[FMEPoint, FMEPoint], bulge: float) -> None:
        """Creates an arc using the 2 points contained in the tuple, and the supplied 'bulge' value.

        All angles are CCW up from the horizontal, and are measured in degrees.

        Args:
            twoPoints (tuple[FMEPoint]): The tuple containing 2 points to create
                the arc in the form (startPoint, endPoint).
            bulge (float): The bulge value for the arc to be created.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(
        self,
        centrePoint: FMEPoint,
        rotation: float,
        primaryRadius: float,
        secondaryRadius: float,
        startAngle: float,
        sweepAngle: float,
    ) -> None:
        """Creates an arc using the center point supplied, along with the
        supplied radii and angles.

        Measures on the center point will be ignored. All angles are CCW up from
        the horizontal, and are measured in degrees.

        Args:
            centrePoint (FMEPoint): The centre point of the arc.
            rotation (float): The rotation angle of the arc.
            primaryRadius (float): The radius of the arc.
            secondaryRadius (float): The secondary radius of the arc.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(
        self,
        centerPoint: FMEPoint,
        rotation: float,
        primaryRadius: float,
        secondaryRadius: float,
        startAngle: float,
        sweepAngle: float,
        startPoint: FMEPoint,
        endPoint: FMEPoint,
    ) -> None:
        """Creates an arc using the center point supplied, along with the
        supplied radii, angles, and points.

        All angles are CCW up from the horizontal, and are measured in degrees.

        Args:
            centrePoint (FMEPoint): The centre point of the arc.
            rotation (float): The rotation angle of the arc.
            primaryRadius (float): The radius of the arc.
            secondaryRadius (float): The secondary radius of the arc.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.
            startPoint (FMEPoint): (optional) The start point of the arc.
            endPoint (FMEPoint): (optional) The end point of the arc.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(
        self,
        twoPoints: tuple[FMEPoint, FMEPoint],
        radius: float,
        counterClockwise: bool,
    ) -> None:
        """Creates an arc using the 2 points contained in the tuple, and the
        supplied 'radius' and points.

        startPoint and endPoint (twoPoints[0] and twoPoints[1]) must not be None.

        Args:
            twoPoints (tuple[FMEPoint]): The tuple containing 2 points to create
                the arc in the form (startPoint, endPoint).
            radius (float): The radius of the arc to be created.
            counterClockwise (bool): Whether the arc is to be drawn counter-clockwise.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(self, arc: FMEArc) -> None:
        """Creates an arc using the supplied arc.

        Args:
            arc (FMEArc): The arc to be copied.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    def bisectArc(self) -> FMEPath:
        """BReturns an equivalent path consisting of two smaller arcs.

        These two arcs do not necessarily have equal length.

        Returns:
            (FMEPath): An equivalent path consisting of two smaller arcs.
        """
    def convertToArcBy3Points(self) -> None:
        """Converts the arc to an arc by 3 points.

        If the arc is not circular (isCircular() returns False), then the arc
        cannot be converted to arc by 3 points, and an error is returned.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertToArcByBulge(self) -> None:
        """Converts the arc to an arc by bulge.

        If the arc is not circular (isCircular() returns False), then the arc
        cannot be converted to arc by bulge, and an error is returned.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertToArcByCenterPoint(self) -> None:
        """Converts the arc to an arc by center point.

        If the arc cannot be converted, then an error is returned.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAsLine(self) -> FMELine:
        """Returns an equivalent line.

        Returns:
            (FMELine): An equivalent line.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to be used to approximate the arc.

        Returns:
            (FMELine): An equivalent line.
        """
    def getBulge(self) -> float:
        """Returns the bulge value of the arc.

        An error is returned if an error occurs.

        Returns:
            (float): The bulge value of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getCenterPoint(self) -> FMEPoint:
        """Returns the center point of the arc.

        An error is returned if an error occurs.

        Returns:
            (FMEPoint): The center point of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getEndPoint(self) -> FMEPoint or None:
        """Returns the end point of the arc.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint): The end point of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the arc.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the length in 3D.

        Returns:
            (float): The length of the arc.
        """
    def getMidpoint(self) -> FMEPoint:
        """Returns mid point, which will be interpolated halfway along the arc if
        the underlying storage is not by 3 points.

        If an arc is elliptical, an error is returned.

        Returns:
            (FMEPoint): The midpoint of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPrimaryRadius(self) -> float:
        """Returns the primary radius of the arc.

        Returns:
            (float): The primary radius of the arc.
        """
    def getPropertiesAs3Points(self) -> tuple[FMEPoint]:
        """Returns the arc geometry as a tuple of three points.

        If the arc is elliptical, an error is returned.

        The structure of the tuple returned is as follows:
            (startPoint, midPoint, endPoint).

        Returns:
            (tuple[FMEPoint]): The arc geometry as three points.
        """
    def getPropertiesAsBulge(self) -> tuple[FMEPoint, FMEPoint, float]:
        """Returns the arc geometry as a tuple of three points and a bulge.

        If the arc is elliptical, an error is returned.

        The structure of the tuple returned is as follows:
            (startPoint, endPoint, bulge).

        Returns:
            (tuple[FMEPoint, FMEPoint, float]): The arc geometry as three points
                and a bulge.
        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPropertiesAsCentered(
        self,
        withEnds: bool,
    ) -> tuple[
        FMEPoint, float, float, float, float, float, FMEPoint, FMEPoint
    ] or tuple[FMEPoint, float, float, float, float, float]:
        """Returns the arc properties.

        If 'withEnds' is True, the end points will be computed and returned.
        Note that measures are only stored on the end points. All angles are CCW
        up from the horizontal, and rotation is measured in degrees. Also, 'startAngle'
        and 'sweepAngle' aren't angles. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of 'startAngle'.

        The structure of the tuple returned if 'withEnds' is True is as follows:
            (centerPoint, rotation, primaryRadius, secondaryRadius,
            startAngle, sweepAngle, startPoint, endPoint).

        The structure of the tuple returned if 'withEnds' is False is as follows:
            (centerPoint, rotation, primaryRadius, secondaryRadius,
            startAngle, sweepAngle).

        Returns:
            (tuple[FMEPoint, float, float, float, float, FMEPoint, FMEPoint]):
                The arc geometry as a centered point definition.
        """
    def getRotation(self) -> float:
        """Returns the rotation of the arc.

        All angles are CCW up from the horizontal, and are measured in degrees.

        Returns:
            (float): The rotation of the arc.
        """
    def getSecondaryRadius(self) -> float:
        """Returns the secondary radius of the arc.

        Returns:
            (float): The secondary radius of the arc.
        """
    def getStartAngle(self) -> float:
        """Returns the start angle of the arc.

        All angles are CCW up from the horizontal.

        Note: 'startAngle' isn't an angle. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of startAngle.

        Returns:
            (float): The start angle of the arc.
        """
    def getStartPoint(self) -> FMEPoint or None:
        """Returns the start point of the arc.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint): The start point of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getSweepAngle(self) -> float:
        """Returns the sweep angle of the arc.

        All angles are CCW up from the horizontal.

        Note: 'startAngle' isn't an angle. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of startAngle.

        Returns:
            (float): The sweep angle of the arc.
        """
    def hasExplicitEndpoints(self) -> bool:
        """This returns True if the arc's end points have been explicitly set, and False otherwise.

        getPropertiesAsCentered() method can calculate the end points if none
        have been specified by setting the 'withEnds' parameter to True. If this
        is not desired, hasExplicitEndpoints can be called first to determine
        whether the 'withEnds' parameter should be set to True or False.

        Returns:
            (bool): Whether the arc has explicit endpoints.
        """
    def isCW(self) -> bool:
        """Returns True if the arc is clockwise, and False otherwise.

        Returns:
            (bool): Whether the arc is clockwise.
        """
    def isCircular(self) -> bool:
        """Returns True if the arc is circular, and False otherwise.

        Returns:
            (bool): Whether the arc is circular.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.

        If 'threeD' is True, the z coordinate of the start and end points will
        be compared. This does not take measures into consideration.

        Returns:
            (bool): True if the start and end point have identical coordinate values,
                False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            (bool): True if the curve contains only lines, False otherwise.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offset the arc by the specified point.

        Args:
            offsetPoint (FMEPoint): The point to offset the arc by.
        """
    def optimalArcTypeRetrieval(self) -> int:
        """Returns the arc type
            (FME_ARC_BY_CENTER_POINT, FME_ARC_BY_CENTER_POINT_START_END,
            FME_ARC_BY_BULGE, or FME_ARC_BY_3_POINTS)
          whose parameters that define the arc can be retrieved most efficiently and accurately.

        Returns:
            (int): The arc type.
        """
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise only x and y are.

        Args:
            checkZ (bool): Whether to check z coordinates.
        """
    def reverse(self) -> None:
        """This reverses the order of the curve's points."""
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """Rotates the arc by the specified angle about the specified point.

        Args:
            centre (FMEPoint): The point to rotate the arc about.
            angle (float): The angle to rotate the arc by.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the arc by the specified factors.

        Args:
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.
            zScale (float): (optional) The z scale factor. Default value is 1.0

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setCenterPoint(self, centerPoint: FMEPoint) -> None:
        """Sets the center point of the arc.

        The arc is converted to an arc by center point as a result of this method.

        Args:
            centerPoint (FMEPoint): The center point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The end point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setMidPoint(self, midPoint: FMEPoint) -> None:
        """Sets the midpoint of the arc.

        It only sets the midpoint if the arc can be successfully converted to
        an arc by mid point.

        Args:
            midPoint (FMEPoint): The mid point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setPrimaryRadius(self, primaryRadius: float) -> None:
        """Sets the primary radius of the arc.

        The arc is converted to an arc by center point before setting the primary radius.

        Args:
            primaryRadius (float): The primary radius of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setRotation(self, rotation: float) -> None:
        """Sets the rotation of the arc.

        The arc is converted to an arc by center point before setting the rotation.

        Args:
            rotation (float): The rotation of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setSecondaryRadius(self, secondaryRadius: float) -> None:
        """Sets the secondary radius of the arc.

        The arc is converted to an arc by center point before setting the secondary radius.

        Args:
            secondaryRadius (float): The secondary radius of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartAngle(self, startAngle: float) -> None:
        """Sets the start angle of the arc, measured counter-clockwise up from the horizontal.

        Note: 'startAngle' is a t angle. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of 'startAngle'.

        Args:
            startAngle (float): The start angle to set on the arc.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setSweepAngle(self, sweepAngle: float) -> None:
        """Sets the sweep angle of the arc, measured counter-clockwise up from the horizontal.

        Note: 'sweepAngle' is a t angle. The arc is first converted to an arc by
        center point before the 'sweepAngle' is set. Refer to the @Arc (function)
        in the FME Functions and Factories manual for a detailed definition of 'sweepAngle'.

        Args:
            sweepAngle (float): The sweep angle to set on the arc.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location.
            endLocation (float): The end location.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same,
        keep two same points.

        Args:
            startPoint (FMEPoint): The start point.
            endPoint (FMEPoint): The end point.
        """

class FMEOrientedArc(FMESegment):
    """FME Oriented Arc Class"""

    @overload
    def __init__(
        self,
        arc: FMEArc,
        startCoord: tuple[float, float, float] or None,
        endCoord: tuple[float, float, float] or None,
        transformationMatrix: list[list[float]],
    ) -> None:
        """Creates an oriented arc using an arc, a start coordinate, a end coordinate, and a transformation matrix.

        The startCoord and endCoord are optional and can be specified as None.

        The transformation matrix can be used to place the oriented arc in a
        custom orientation and location as follows:

            Pick three orthogonal unit vectors V1, V2, V3 which represents the
            X, Y, and Z axes of the orientation, and a vector v4 that represents
            the offset of the arc. Then, the transformation matrix is of the
            form: [[V1x,V1y,V1z,0x],[V2x,V2y,V2z,0x],[V3x,V3y,V3z,0x],[0,0,0,1]]

            The matrix can be any kind of affine transformation matrix. Only
            three rows are expected in the input array, as a bottom row of
            [ 0 0 0 1 ] is assumed. The end result of this call will be forced
            to 3D if the input arc is 3D.

        Args:
            arc (FMEArc): The arc to use for creating the oriented arc.
            startCoord (tuple[float,float,float] or None): The start coordinate
                of the oriented arc in the form (x, y, z). The z is not required
                and will be ignored when the input arc is 2D. This is optional
                and can be specified as None.
            endCoord (tuple[float,float,float] or None): The end coordinate of
                the oriented arc in the form (x, y, z). The z is not required
                and will be ignored when the input arc is 2D. This is optional
                and can be specified as None.
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the created oriented arc, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom row
                of [ 0 0 0 1 ] is assumed.

        Returns:
            (FMEOrientedArc): The oriented arc.
        """
    @overload
    def __init__(self, orientedArc: FMEOrientedArc) -> None:
        """Creates an oriented arc using an oriented arc.

        Args:
            orientedArc (FMEOrientedArc): The oriented arc to use for creating the oriented arc.

        Returns:
            (FMEOrientedArc): The oriented arc.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArcInLocalCoordinates(self) -> FMEArc:
        """Returns the FMEArc contained within this oriented arc, in local coordinates.

        Returns:
            (FMEArc): The arc in local coordinates.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getArea(self) -> float: ...
    def getAsLine(self) -> FMELine: ...
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine: ...
    def getEndPoint(self) -> FMEPoint or None: ...
    def getLength(self, threeD: bool) -> float: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValues(self, measureName: str) -> tuple[float]:
        """Returns the values of the specified measures.

        Args:
            measureName (str): The name of the measure to get the values of.

        Returns:
            (tuple[float]): The values of the specified measures.

        Raise:
            FMEException: An exception is raised if an error occurred.
        """
    def getName(self) -> text_type or None: ...
    def getStartPoint(self) -> FMEPoint or None: ...
    def getTrait(self, traitName: str) -> text_type or None: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this oriented arc's transformation matrix.

        If the oriented arc does not have such a matrix, an identity matrix is
        returned. Only the top three rows of the matrix will be returned, as the
        bottom row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The oriented arc's transformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTrandformationMatrix(self) -> bool:
        """Returns True if this oriented arc has a transformation matrix.

        Returns:
            (bool): True if this oriented arc has a transformation matrix.
        """
    def is3D(self) -> bool: ...
    def isClosed(self, threeD: bool) -> bool: ...
    def isCollection(self) -> bool: ...
    def isLinear(self) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this oriented arc's transformation matrix."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setArc(self, arc: FMEArc, transformationMatrix: list[list[float]]) -> None:
        """Sets the arc of this oriented arc.

        The input arc should be planar. The existing arc will be replaced and
        the transformation matrix will be reset to the given value. To leave the
        transformation matrix in place and modify the arc's local coordinates only,
        use setArcInLocalCoordinates(). If the input arc is None, then an exception
        will be raised.

        Args:
            arc (FMEArc): The arc to use for creating the oriented arc.
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the created oriented arc, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom row
                of [ 0 0 0 1 ] is assumed.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcInLocalCoordinate(self, arc: FMEArc) -> None:
        """Sets the arc of this oriented arc.

        The input arc should be planar. If the input arc is None, then an exception
        will be raised.

        Args:
            arc (FMEArc): The arc to set on this oriented arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setEndPoint(self, point: FMEPoint) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setStartPoint(self, point: FMEPoint) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, transformationMatrix: list[list[float]]) -> None:
        """Sets this oriented arc's transformation matrix.

        Only the top three rows of the matrix will be used, as the bottom row is
        always [ 0 0 0 1 ].

        Args:
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the oriented arc, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom row
                of [ 0 0 0 1 ] is assumed.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None: ...
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None: ...

class FMEClothoid(FMESegment):
    """FME Clothoid Class"""

    @overload
    def __init__(
        self,
        startPoint: FMEPoint,
        endPoint: FMEPoint,
        transformationMatrix: list[list[float]],
        localStartCoord: tuple[float, float, float],
        localEndZ: float,
        startDirection: float,
        startCurvature: float,
        endCurvature: float,
        localLength: float,
    ) -> None:
        """
        Creates a clothoid.

        The startPoint and endPoint are optional and can be specified as None.

        The transformation matrix can be used to place the clothoid in a custom
        orientation and location as follows:

            Pick three orthogonal unit vectors V1, V2, V3 which represents the
            X, Y, and Z axes of the orientation, and a vector v4 that represents
            the offset of the arc. Then, the transformation matrix is of the
            form: [[V1x,V1y,V1z,0x],[V2x,V2y,V2z,0x],[V3x,V3y,V3z,0x],[0,0,0,1]]

            The matrix can be any kind of affine transformation matrix. Only
            three rows are expected in the input array, as a bottom row of
            [ 0 0 0 1 ] is assumed.

        Args:
            startPoint (FMEPoint): The start point of the clothoid. It is optional
                and can be specified as None.
            endPoint (FMEPoint): The end point of the clothoid. It is optional
                and can be specified as None.
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the created clothoid, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom
                row of [ 0 0 0 1 ] is assumed.
            localStartCoord (tuple[float, float, float]):  The XYZ (in local
                coordinates) of the clothoid's start coordinate in the form (x, y, z).
            localEndZ (float): The elevation (in local coordinates) of the
                clothoid's end coordinate.
            startDirection (float): The start angle (in degrees of the local
                coordinates) of the clothoid.
            startCurvature (float): The start curvature (in local coordinates) of the clothoid.
            endCurvature (float): The end curvature (in local coordinates) of the clothoid.
            localLength (float): The length (in local coordinates) of the clothoid.

        Returns:
            (FMEClothoid): The created clothoid.
        """
    @overload
    def __init__(safe, clothoid: "FMEClothoid") -> None:
        """
        Creates a clothoid from another clothoid.

        Args:
            clothoid (FMEClothoid): The clothoid to copy.

        Returns:
            (FMEClothoid): The created clothoid.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getAsLine(self) -> FMELine: ...
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine: ...
    def getEndCurvature(self) -> float:
        """
        Returns the end curvature (in local coordinates) of the clothoid.

        Returns:
            (float): The end curvature (in local coordinates) of the clothoid.
        """
    def getEndPoint(self) -> FMEPoint: ...
    def getLength(self, threeD: bool) -> float: ...
    def getLocalEndZ(self) -> float:
        """Returns the elevation (in local coordinates) of the clothoid's end coordinate.

        If the clothoid is 2D, the z value will be given as NaN.

        Returns:
            (float): The elevation (in local coordinates) of the clothoid's end
                coordinate.
        """
    def getLocalLength(self) -> float: ...
    def getLocalStartCoordXY(self) -> tuple[float, float]:
        """
        Returns the XY (in local coordinates) of the clothoid's start coordinate.

        Returns:
            (tuple[float,float]): The XY (in local coordinates) of the clothoid's start coordinate.
        """
    def getLocalStartCoordXYZ(self) -> tuple[float, float, float]:
        """
        Returns the XYZ (in local coordinates) of the clothoid's start coordinate.

        Returns:
            (tuple[float,float,float]): The XYZ (in local coordinates) of the clothoid's start coordinate.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValues(self, measureName: str) -> tuple[float, float]:
        """
        Returns the values of the specified measure.

        Args:
            measureName (str): The name of the measure.

        Returns:
            (tuple[float,float]): The values of the named measure in the form
                (start_point_value, end_point_value)
        """
    def getName(self) -> text_type or None: ...
    def getStartCurvature(self) -> float:
        """
        Returns the start curvature (in local coordinates) of the clothoid.

        Returns:
            (float): The start curvature (in local coordinates) of the clothoid.
        """
    def getStartDirection(self) -> float:
        """
        Returns the start angle (in degrees of the local coordinates) of the clothoid.

        Returns:
            (float): The start angle (in degrees of the local coordinates) of the clothoid.
        """
    def getStartPoint(self) -> FMEPoint or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this clothoid's transformation matrix.

        If the clothoid does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom row
        is always [ 0 0 0 1 ].

        Returns:
          (list[list[float]]): The transformation matrix of the clothoid.
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTransformationMatrix(self) -> bool:
        """
        Returns True if the clothoid has a transformation matrix.

        Returns:
            (bool): True if the clothoid has a transformation matrix.
        """
    def is3D(self) -> bool: ...
    def isClosed(self, threeD: bool) -> bool: ...
    def isCollection(self) -> bool: ...
    def isLinear(self) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes the transformation matrix of the clothoid."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndCurvature(self, endCurvature: float) -> None:
        """
        Sets the end curvature (in local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            endCurvature (float): The end curvature (in local coordinates) of the clothoid.
        """
    def setEndPoint(self, point: FMEPoint) -> None: ...
    def setLength(self, localLength: float) -> None:
        """
        Sets the length (in local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            localLength (float): The length (in local coordinates) of the clothoid.
        """
    def setLocalEndZ(self, localEndZ: float) -> None:
        """
        Sets the elevation (in local coordinates) of the clothoid's end coordinate.

        Args:
            localEndZ (float): The elevation (in local coordinates) of the clothoid's end
                coordinate.
        """
    def setLocalStartCoordXY(self, xCoord: float, yCoord: float) -> None:
        """
        Sets the XY (in local coordinates) of the clothoid's start coordinate.

        This will recompute the end point.

        Args:
            xCoord (float): The X coordinate (in local coordinates) of the clothoid's start coordinate.
            yCoord (float): The Y coordinate (in local coordinates) of the clothoid's start coordinate.
        """
    def setLocalStartCoordXYZ(
        self, xCoord: float, yCoord: float, zCoord: float
    ) -> None:
        """
        Sets the XYZ (in local coordinates) of the clothoid's start coordinate.

        This will recompute the end point.

        Args:
            xCoord (float): The X coordinate (in local coordinates) of the clothoid's start coordinate.
            yCoord (float): The Y coordinate (in local coordinates) of the clothoid's start coordinate.
            zCoord (float): The Z coordinate (in local coordinates) of the clothoid's start coordinate.
        """
    def setMeasure(
        self, measureName: str, startPointValue: float, endPointValue: float
    ) -> None:
        """
        Assign the given values to the specified measure. This will create the measure if it doesn't already exist.

        Args:
            measureName (str): The name of the measure.
            startPointValue (float): The value of the measure at the start point.
            endPointValue (float): The value of the measure at the end point.
        """
    def setName(self, name: text_type) -> None: ...
    def setStartCurvature(self, startCurvature: float) -> None:
        """
        Sets the start curvature (in local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            startCurvature (float): The start curvature (in local coordinates) of the clothoid.
        """
    def setStartDirection(self, startDirection: float) -> None:
        """
        Sets the start angle (in degrees of the local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            startDirection (float): The start angle (in degrees of the local coordinates) of the clothoid.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """
        Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point of the clothoid.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, transformationMatrix: list[list[float]]) -> None:
        """
        Sets this clothoid's transformation matrix, replacing the existing matrix if it exists.

        Only three rows are expected in the input array, as a bottom row of
        [ 0 0 0 1 ] is assumed.

        Args:
            transformationMatrix (list[list[float]]): The transformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None: ...
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None: ...

# removeTraits() Constants¶
kFME_RecurseAll: int
kFME_RecurseSome: int

class FMEGeometryIterator:
    """FMEGeometryIterator Class

    FMEGeometryIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEAggregate to get an FMEGeometryIterator which can
    be used to iterate over its geometries.
    """

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEGeometry:
    """FME Geometry Class"""

    def __init__(self) -> None:
        """Default FMEMesh constructor.

        Returns:
            (FMEMesh): An instance of a Mesh geometry object.
        """
    def boundingBox(self) -> tuple[tuple[float]]:
        """Returns the bounding box of the mesh.

        Returns:
            (tuple[tuple[float]]): The bounding box of the Geometry, in the
                form ((minx, miny), (maxx, maxy)).
        """
    def boundingCube(self) -> tuple[tuple[float]]:
        """Returns the bounding cube of the mesh.

        Returns:
            (tuple[tuple[float]]): The bounding cube of the Geometry, in the
                form ((minx, miny, minz), (maxx, maxy, maxz)).
        """
    def bounds(self) -> tuple[FMEPoint]:
        """Returns the bounds of the mesh.

        Returns:
            (tuple[FMEPoint]): The min point and max point of the bounds.
                None is returned if the geometry contains no points.
        """
    def clearMeasures(self) -> None:
        """Clears all measures from the mesh."""
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None:
        """Copies all the attributes from the given feature to traits on this
        geometry, if they match the (optional) regular expression.

        Args:
            sourceFeature (FMEFeature): The source feature to copy attributes from.
            overwriteExisting (bool): Existing traits will be overwritten only
                if overwriteExisting is True.
            regexp (str):  (Optional) The regular expression to match the
                attributes against. If regexp is not specified, then all
                attributes will be copied.
            prefix (str): (Optional) The prefix is put on all the trait names as
                they are copied. If it is not specified, a prefix will not be
                added to the trait names.
        """
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None:
        """Copies the name from the given geometry to this geometry.

        If 'sourceGeometry's name is blank or None, this geometry's name will
        become None.

        Args:
            sourceGeometry (FMEGeometry): The source geometry to copy the name from.
        """
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None:
        """Copies all the traits from the given geometry that match the (optional)
        regular expression.

        Args:
            sourceGeometry (FMEGeometry): The source geometry to copy traits from.
            overwriteExisting (bool): Existing traits will be overwritten only
                if overwriteExisting is True.
            regexp (str):  (Optional) The regular expression to match the traits
                against. If regexp is not specified, then all traits will be copied.
            prefix (str): (Optional) The prefix is put on all the trait names as
                they are copied. If it is not specified, a prefix will not be
                added to the trait names.
        """
    def copyTraitsToFeature(
        self,
        destFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None:
        """Copies all the traits from this geometry to attributes on the given
        feature, if they match the (optional) regular expression

        Args:
            destFeature (FMEFeature): The destination feature to copy traits to.
            overwriteExisting (bool): Existing traits will be overwritten only
                if overwriteExisting is True.
            regexp (str):  (Optional) The regular expression to match the traits
                against. If regexp is not specified, then all traits will be copied.
            prefix (str): (Optional) The prefix is put on all the trait names as
                they are copied. If it is not specified, a prefix will not be
                added to the trait names.
        """
    def deleteName(self) -> bool:
        """Deletes the name of the geometry.

        If a name existed prior to this call then True is returned; otherwise
        False is returned.

        Returns:
            (bool): Returns a boolean indicating whether or not the name existed
                before deletion.
        """
    def force2D(self) -> None:
        """Reduces the geometry to be 2D."""
    def force3D(self, newZ: float) -> None:
        """This sets the geometry's dimension to 3D.

        All Z values are set to the value passed in, even if the geometry is
        already 3D.

        Args:
            newZ (float): The z coordinate to use for the new geometry.
        """
    def getArea(self) -> float:
        """Area calculation.

        Returns:
            (float): The calculated area.
        """
    def getMeasureNames(self) -> tuple[str]:
        """Retrieve the names of the measures on this geometry.

        Returns:
            (tuple[string]): Return a tuple storing the names of the measures on
                this geometry. This will return an empty tuple if there are no
                measures. For FMEAggregate, FMEMultiSurface, and
                FMECompositeSurface, this will return the union of all measure
                names of all of its parts.
        """
    def getName(self) -> text_type or None:
        """This routine retrieves the 'name' of this geometry as a six.text_type.

        This will return None if it did not have a name associated with it.

        Returns:
            (six.text_type or None): The geometry's name.
        """
    def getTrait(
        self,
        traitName: str,
    ) -> bool or int or float or string_types or bytearray or bytes or None:  # type: ignore
        """Retrieves the geometry trait value of the specified trait name.

        Null trait values will be returned as an empty string.
        Binary blob traits are returned as a bytearray.

        Args:
            traitName (str): The name of the geometry trait.

        Returns:
            (bool or int or float or six.string_types or bytearray or bytes or None):
                The trait value.

        Raises:
            FMEException: An exception is raised if there was a problem in
                retrieving the trait value.
        """
    def getTraitNames(self) -> tuple[str]:
        """Retrieves the names of the traits on this geometry.

        Returns:
            (tuple[str]): Return a tuple storing the names of the traits on this
                geometry. This will return an empty tuple if there are no traits.
                For all collections and containers, this will only return the
                names of traits on the outermost object only.
        """
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]:
        """This method returns a tuple of a boolean, indicating if the trait is
        null, a boolean, indicating if the trait is missing, and an integer
        representing the type of the trait.

        The first boolean is True if 'traitName' maps to a null trait value on
        the geometry. Otherwise it is False. The second boolean is True if
        'traitName' maps to a no value on the geometry. Otherwise it is False.
        If the trait is absent, FME_ATTR_UNDEFINED is returned for the type.

        The possible trait types are FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
        FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
        FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
        FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64,
        FME_ATTR_UINT64.

        Args:
            traitName (str): The trait's name.

        Returns: tuple[bool, bool, int]: A tuple of 2 boolean values the first
            indicating whether or not the value of the trait is null, the second
            indicating whether or not the trait is missing, and an integer
            representing the trait type.
        """
    def getTraitType(self, traitName: str) -> int:
        """This method returns the type of the trait.

        If the trait cannot be found, FME_ATTR_UNDEFINED will be returned.

        Returns one of  FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN, FME_ATTR_INT8,
        FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16, FME_ATTR_INT32,
        FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64, FME_ATTR_REAL80,
        FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64, FME_ATTR_UINT64.

        Args:
            traitName (str): The trait's name.

        Returns:
            (int): The type of the trait.
        """
    def hasMeasures(self) -> bool:
        """Check if this geometry or any sub part of this geometry has measures.

        Returns:
            (bool): True if this geometry or any sub part of this geometry has
                measures, False otherwise.
        """
    def hasName(self) -> bool:
        """Check if this geometry has a name.

        Returns:
            (bool): True if this geometry has a name, False otherwise.
        """
    def is3D(self) -> bool:
        """Check if this geometry is 3D.

        Returns:
            (bool): Returns True if the geometry is 3D and False otherwise. For
                FMENull, this method will always return True. For FMEAggregate,
                FMEMultiPoint, FMEMultiArea, FMEMultiText and FMEMultiCurve,
                this method will return True if any one of the sub-parts is 3D.
                If the collection is empty or all of its members are 2D, this
                method will return False.
        """
    def isCollection(self) -> bool:
        """Check if the geometry is an aggregate or multi-part collection.

        Returns:
            (bool): True if the geometry is an aggregate or multi-part collection,
                False otherwise.
        """
    def measureExists(self, measureName: str) -> bool:
        """CReturns True if the specified measure exists and False otherwise.

        If the 'measureName' parameter is not specified then the default measure
        is checked.

        Returns:
            (bool): Boolean indicating whether or not the measure exists.
        """
    def removeMeasure(self, measureName: str) -> None:
        """Removes the measure with name 'measureName' if supplied, or the
        default measure, if there is one.

        Args:
            measureName (str): (Optional) The name of the measure to remove.
        """
    def removeTraits(self, regexp: str) -> None:
        """Removes all traits that match the given regular expression.

        This method has 4 modes:
            Remove all traits at the top level: regex == NULL
            Remove some traits at the top level: regex == <string>
            Remove all traits at all levels: regex == kFME_RecurseAll
            Remove some traits at all levels: regex == kFME_RecurseSome <string>

        For example, specifying regex == NULL for a multi-surface will remove
        all traits at the root level of the multi-surface, whereas specifying
        regex == kFME_RecurseSome <string> will remove all traits from all
        levels of the multi surface that match <string>. If <string> is an
        illegal regular expression, no traits will be removed.
        """
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None:
        """Renames the measure with name 'oldMeasureName' to 'newMeasureName'.

        Args:
            oldMeasureName (str): The name of the measure to rename.
            newMeasureName (str): The new name of the measure.
        """
    def setName(self, name: text_type) -> None:
        """Sets the geometry's name with a six.text_type.

        By supplying a blank name as input, this method will act as deleteName().

        Args:
            name (six.text_type): The name to set.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None:
        """Sets a geometry trait with the specified value.

        If the geometry trait already exists, its value and type will be changed.
        The following type numeric mappings are used:
            PyInt ==> FME_Int32
            PyFloat ==> FME_Real64
            PyLong ==> FME_Int64

        For Python 2.7, strings can be input as one of two possible types:
        system encoded strings or unicode strings. Binary values are to be
        specified as bytearray values or bytes values for Python 3 and as
        bytearray values for Python 2.7.

        Args:
            traitName (str): The name of the trait to set.
            traitValue (bool or int or float or six.text_type or bytearray or bytes): The value of the trait.
        """
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None:
        """This method supplies a null trait value with a type to the geometry.

        If a trait with the same name already exists, it is overwritten.

        Trait type must be one of FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
        FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
        FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
        FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64,
        FME_ATTR_UINT64.

        Args:
            traitName (str): The name of the trait to set.
            traitType (int): The type of the trait.
        """

class FMENull(FMEGeometry):
    """FME Null Class"""

    def __init__(self, null: FMENull) -> None:
        """Create a copy of the passed in Null geometry object.

        Args:
            mesh (FMENull): The Null geometry object to create a copy of.

        Returns:
            (FMENull): An instance of a Null Geometry object.
        """

class FMEAggregate(FMEGeometry):
    """FME Aggregate Class"""

    def __init__(self, aggregate: FMEAggregate) -> None:
        """Create a copy of the passed in Aggregate geometry object.

        Args:
            mesh (FMEAggregate): The Aggregate geometry object to create a copy of.

        Returns:
            (FMEAggregate): An instance of a Aggregate Geometry object.
        """
    def appendPart(self, geometry: FMEGeometry) -> None:
        """This appends the geometry to the aggregate.

        If None is passed in, nothing will be appended. Note that the geometries
        stored in an aggregate may have different dimensions. Calling this method
        will implicitly apply and clear any matrix associated with this aggregate.

        Args:
            geometry (FMEGeometry): The geometry to be appended.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendPartInLocalCoordinates(self, geometry: FMEGeometry) -> None:
        """This appends the geometry to the aggregate in local coordinates.

        If None is passed in, nothing will be appended. Note that the geometries
        stored in an aggregate may have different dimensions. Calling this method
        will leave any matrix associated with the aggregate intact, meaning the
        new part will have any matrix applied.

        Args:
            geometry (FMEGeometry): The geometry to be appended.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendParts(self, aggregate: FMEAggregate) -> None:
        """This appends the aggregate of geometries passed in to the aggregate.

        If None is passed in, nothing will be appended. Calling this method will
        implicitly apply and clear any matrix associated with this aggregate.

        Args:
            aggregate (FMEAggregate): The aggregate of geometries to be appended.


        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAppearanceReference(self, front: bool) -> int:
        """This method returns the appearance reference within the Library associated with this aggregate.

        The 'front' parameter controls whether this query should return the
        front or the back appearance reference. Both can be fetched independently.
        If this aggregate is a regular aggregate with no geometry instance, a
        FMEException will be thrown.

        Args:
            front (bool): Boolean indicating whether the appearance reference
                should be retrieved for the front or back of the aggregate.

        Returns:
            (int): The unique appearance reference for this appearance.
        """
    def getGeometryDefinitionReference(self) -> int or None:
        """This method will get the geometry definition reference associated with
        this aggregate, if this aggregate is a geometry instance.

        If this aggregate is a regular aggregate with no geometry instance, None
        will be returned.

        Returns:
            (int): The geometry definition reference, or None.
        """
    def getGeometryInstanceLocalOrigin(self) -> list[list[float]] or None:
        """This method retrieves the local origin associated with the geometry
        instance, if this aggregate is a geometry instance.

        This method will return None if the aggregate is a regular aggregate.

        Returns:
            (list[list[float]]): The local origin, formatted (ddd), or None.
        """
    def getGeometryInstanceMatrix(self) -> list[list[float]] or None:
        """This method retrieves the geometry instance transformation matrix
        associated with the geometry instance, if this aggregate is a geometry
        instance.

        This method will return None if the aggregate either contains
        no such matrix or is a regular aggregate.

        Returns:
            (list[list[float]]): The geometry instance transformation matrix,
                formatted [[dddd][dddd][dddd]], or None.
        """
    def getMultipleGeometryFlag(self) -> bool:
        """This method determines if the aggregate contains a MultipleGeometry,
        that is, whether the aggregate is structured in a way such that each part
        is its own geometry separate from the other parts in the aggregate.

        As a result, it is possible for an aggregate of 1 part to return true
        since it is about the structure of the aggregate, and not the content.

        Returns:
            (bool): Returns True if the aggregate contains a multiple geometry
            and False otherwise.
        """
    def getPartAt(self, index: int) -> FMEGeometry or None:
        """This method returns the geometry at the given index.

        None is returned if the index is out of range. For an aggregate with a
        transformation matrix, the transformed geometry is returned.

        Args:
            index (int): The index of the geometry to be returned.

        Returns:
            (FMEGeometry): The geometry at the given index. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one of the
                leaf classes in the FMEGeometry inheritance graph. For example, a
                FMEPoint is returned if the geometry truly is a point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPartAtInLocalCoordinates(self, index: int) -> FMEGeometry or None:
        """This method returns the geometry at the given index.

        None is returned if the index is out of range. For an aggregate with a
        transformation matrix, it will NOT be applied to the part.

        Args:
            index (int): The index of the geometry to be returned.

        Returns:
            (FMEGeometry): The geometry at the given index. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one
                of the leaf classes in the FMEGeometry inheritance graph. For
                example, a FMEPoint is returned if the geometry truly is a point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this aggregate's transformation matrix.

        If the aggregate does not have such a matrix, an identity matrix is
        returned. Only the top three rows of the matrix will be returned, as the
        bottom row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The aggregate's tranformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def hasGeometryInstance(self, recursive: bool) -> bool:
        """This method returns True if this aggregate contains an instance of a
        geometry definition.

        If the parameter recursive is set to False, it will only test this
        aggregate itself. If 'recursive' is equal to True, then this method will
        return True if any part contained in this aggregate at any level is a
        geometry instance.

        Args:
            recursive (bool): To recurse or not.

        Returns:
            (bool): Whether there is geometry instance.
        """
    def hasTransformationMatrix(self) -> bool:
        """This method returns True if this aggregate has a transformation
        matrix.

        Returns:
            (bool): Whether there is a transformation matrix.
        """
    def isAMulti(self) -> bool:
        """This method determines if the aggregate's parts conform to a
        FMEMultiCurve, FMEMultiArea, or FMEMultiText, representation.

        Returns:
            (bool): This means that it will only return True if the aggregate contains:
                Arcs, Lines, Paths, and nothing else.

                Polygons, Ellipses, Donuts, and nothing else.

                Text objects and nothing else.

                Points and nothing else. This returns false for empty aggregates.
        """
    def isSimpleAggregate(self) -> bool:
        """This method determines if the aggregate is a simple aggregate.

        i.e. that none of its geometries are an Aggregate or Multi.

        Returns:
            (bool): Whether this aggregate is a simple aggregate.
        """
    def numParts(self) -> int:
        """This method returns the number of parts in the aggregate.

        Returns:
            (int): The number of parts in the aggregate.
        """
    def offset(self, point: FMEPoint) -> None:
        """Offsets the geometry by the coords specified by 'point'.

        The offset will be applied to the transformation matrix associated with
        this aggregate. If the aggregate has no matrix, a new matrix will be created.

        Args:
            point (FMEPoint): The point to offset the coordinates of the geometry by.
        """
    def removeLastPart(self) -> FMEGeometry or None:
        """This removes and returns the last geometry of the aggregate.

        If there are no geometries in the aggregate, it will return None. Calling
        this method will implicitly apply and clear any matrix associated with
        this aggregate.

        Returns:
            (FMEGeometry): The last geometry of the aggregate. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one of
                the leaf classes in the FMEGeometry inheritance graph. For
                example, a FMEPoint is returned if the geometry truly is a point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeTransformationMatrix(self) -> None:
        """Removes this aggregate's transformation matrix."""
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """The angle is CCW up from the horizontal and is measured in degrees.

        The rotation will be applied to the transformation matrix associated
        with this aggregate. If the aggregate has no matrix, a new matrix will
        be created.

        Args:
            center (FMEPoint): The center of the rotation.
            angle (float): The angle of the rotation in degrees

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, xscale: float, yscale: float, zscale: float) -> None:
        """Applies a scale factor to the aggregate.

        The scale factor will be applied to the transformation matrix associated
        with this aggregate. The 'zscale' is ignored if geometry is 2D. If the
        aggregate has no matrix, a new matrix will be created.

        Args:
            xscale (float): The x-scale factor.
            yscale (float): The y-scale factor.
            zscale (float): The z-scale factor.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None:
        """This method associates an appearance within the Library with this aggregate.

        This is done by passing in the unique appearance reference for this
        appearance. Subsequent calls to this method on the same side, will
        override the previous appearance used with the new appearance passed in.

        An appearance reference of '0' represents the default appearance.
        Interpretation of the default appearance is left to the consumer of this
        geometry. When set at this FMEAggregate level, the appearance represents
        the default appearance to apply when the contained surfaces use the
        default appearance instead of a specific appearance. Contained surfaces
        may be found within nested aggregates, geometry instances that reference
        geometries containing surfaces, or as surfaces or multi-surfaces.

        The second parameter controls whether this action should take place on
        the front of the contained surfaces or the back. Both can be set
        independently. The 'appearanceRef' should be a valid reference to a
        definition stored in the FMELibrary. If the reference was not found in
        the library, it will still attach the reference to the instance, but
        will throw a FMEException. This is an unhealthy situation as it
        represents a 'dangling reference'.

        Args:
            appearanceRef (int): The unique appearance reference for this appearance.
            front (bool): Whether the appearance is for the front or back of the
                geometry.

        Raises:
            FMEException: An exception is raised if an error occurred or the
            reference was not found in the library and a dangling reference was
            attached.
        """
    def setGeometryDefinitionReference(self, gdReference: int) -> None:
        """This method sets the geometry definition reference of this aggregate.

        If this aggregate is not currently a geometry instance, this call will
        cause the aggregate to destroy all owned parts and turn the aggregate
        into a geometry instance.

        If 'gdReference' reference was not found in the library, it will still
        attach the reference to the instance, but will this is an unhealthy
        situation as it represents a 'dangling reference' and the user should
        decide to remedy this by either adding a Geometry Definition with that
        exact reference to the library, or else remove the reference from this
        geometry instance.

        Args:
            gdReference (int): A valid geometry definition reference to a
            geometry definition stored in the FMELibrary.

        Raises:
            FMEException: An exception is raised if an error occurred or the
              reference was not found in the library and a dangling reference
              was attached.
        """
    def setGeometryInstanceLocalOrigin(self, x: float, y: float, z: float) -> None:
        """Sets the local origin of the geometry instance.

        If this aggregate is not currently a geometry instance, this call will
        cause the aggregate to destroy all owned parts and turn the aggregate
        into a geometry instance. The local origin is the origin from which the
        geometry instance transformation matrix is applied. The default local
        origin is (0,0,0).

        Args:
            x (float): The x-coordinate of the local origin.
            y (float): The y-coordinate of the local origin.
            z (float): The z-coordinate of the local origin.
        """
    def setGeometryInstanceMatrix(self, matrix: list[list[float]]) -> None:
        """Sets the transformation matrix of the geometry instance.

        If this aggregate is not currently a geometry instance, this call will
        cause the aggregate to destroy all owned parts and turn the aggregate
        into a geometry instance. The transformation matrix is applied to the
        geometry definition from the local origin to obtain the instantiated geometry.

        Args:
            matrix (list[list[float]]): The geometry instance transformation
                matrix, formatted [[dddd][dddd][dddd]].
        """
    def setMultipleGeometryFlag(self, isMultiple: bool) -> None:
        """This method sets whether the aggregate contains a MultipleGeometry.

        That is, whether the aggregate is structured in a way such that each
        part is its own geometry separate from the other parts in the aggregate.

        Args:
            isMultiple (bool): True if the aggregate contains a MutlipleGeometry
        """
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets or replaces the transformation matrix of the aggregate.

        If this aggregate has no matrix, a new matrix will be created.
        Only three rows are expected in the input array, as a bottom row of
        [ 0 0 0 1 ] is assumed.

        Args:
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].
        """

class OrientMixin:
    def isOriented(self, orientation: int) -> bool:
        """Returns True if the geometry is oriented in the specified direction.

        Args:
            orientation: (int): The direction to check.

        Returns:
            bool: True if the geometry is oriented in the specified direction.
        """
    def orient(self, orientation: int) -> None:
        """Reorients the geometry such that either all the surface normals face out
        from the  geometry or all the surface normals face in to the geometry.

        Args:
            orientation: (int): The direction to orient the solid in.
        """
    def reorient(self) -> None:
        """Flips the underlying surfaces that make up the geometry, such that the
        front and back of each surface is switched. This has the effect of flipping
        the geometry inside-out. The front and back vertex normals are swapped."""

class TransformMixin:
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offset the geometry by the specified amount.

        Args:
            offsetPoint: (FMEPoint): The offset point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates this geometry about the z-axis by the specified angle, in degrees.

        The rotation is performed relative to the center specified. A positive
        angle corresponds to a counter-clockwise rotation, when looking down onto
        the XY-plane.

        Args:
            center: (FMEPoint): The center of rotation.
            angle: (float): The angle of rotation.
        """
    def reverse(self) -> None:
        """This reverses the order of the geometry's points."""
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales this geometry by the specified factors.

        Args:
            xScale: (float): The x-axis scale factor.
            yScale: (float): The y-axis scale factor.
            zScale: (float): The z-axis scale factor.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class AppearanceMixin:
    def getAppearanceReference(self, front: bool) -> int:
        """Returns the appearance reference for this geometry.

        Args:
            front: (bool): True if the front appearance reference should be returned,
                False if the back appearance reference should be returned.

        Returns:
            int: The appearance reference.
        """
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None:
        """This method associates an appearance within the Library with this solid.
        This is done by passing in the unique appearance reference for this
        appearance. Subsequent calls to this method on the same side, will override
        the previous appearance used with the new appearance passed in.

        An appearance reference of '0' represents the default appearance.
        Interpretation of the default appearance is left to the consumer of this
        geometry. When set at this FMESolid level, the appearance represents the
        default appearance to apply when the contained surfaces use the default
        appearance instead of a specific appearance. Contained surfaces may be
        found within nested solids, geometry instances that reference geometries
        containing surfaces, or as surfaces or multi-surfaces.

        The second parameter controls whether this action should take place on
        the front of the contained surfaces or the back. Both can be set
        independently. The 'appearanceRef' should be a valid reference to a
        definition stored in the FMELibrary. If the reference was not found in
        the library, it will still attach the reference to the instance, but
        will throw a FMEException. This is an unhealthy situation as it represents
        a 'dangling reference'.

        Args:
            appearanceRef: (int): The appearance reference to set.
            front: (bool): True if the front appearance reference should be set,
                False if the back appearance reference should be set.

        Raises:
            FMEException: An exception is raised if an error occurred or the
                reference was not found in the library and a dangling reference
                was attached.
        """

class FMEPointIterator:
    """FME Point Iterator Class"""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEPoint(FMEGeometry):
    """FME Point Class"""

    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        """Creates a point with the given xyz coordinates.

        Args:
            x (float): The x coordinate of the point.
            y (float): The y coordinate of the point.
            z (float): The z coordinate of the point.


        Returns:
          (FMEPoint): An instance of a Point Geometry object.
        """
    @overload
    def __init__(self, point: FMEPoint) -> None:
        """Creates a point from an existing point.

        Args:
            point (FMEPoint): The Point geometry object to create a copy of.


        Returns:
          (FMEPoint): An instance of a Point Geometry object.
        """
    def equalCoordinate(self, point: FMEPoint, checkZ: bool) -> bool:
        """Returns True if the two points have the identical coordinate.

        Z coordinate values are checked only if 'checkZ' is True.
        Measures are not compared.

        Args:
            point (FMEPoint): The Point geometry object to compare with.
            checkZ (bool): If True, the z coordinate is also checked.


        Returns:
          (bool): True if the coordinates are equal, False otherwise.
        """
    def equalOrientation(self, point: FMEPoint) -> bool:
        """Returns True if the two points have identical rotations.

        Measures are not compared.

        Args:
            point (FMEPoint): The Point geometry object to compare with.


        Returns:
          (bool): True if the two points have identical rotations, False otherwise.
        """
    def equals(self, point: FMEPoint) -> bool:
        """Returns True if the two points have the identical coordinate and measures.

        Args:
            point (FMEPoint): The Point geometry object to compare with.


        Returns:
          (bool): True if the two points have identical coordinate and measures,
          False otherwise.
        """
    def getXYZ(self) -> tuple[float]:
        """Returns the xyz coordinates of the point.

        0.0 is returned for the z value if the point is 2D.

        Returns:
          (tuple[float]): The xyz coordinates of the point.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coords specified by 'offsetPoint'.

        Args:
            offsetPoint (FMEPoint): The offset point.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def reset(self, point: FMEPoint) -> None:
        """Set the coordinate and measure values to the values in the given point.

        The point is forced to 3D if necessary. All existing measures are lost.

        Args:
            point (FMEPoint): The point to reset the coordinate and measure values to.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates the point around the given center.

        Args:
            center (FMEPoint): The center of rotation.
            angle (float): The angle to rotate by. The angle is counter-clockwise
            up from the horizontal, and measured in degrees.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """zScale is ignored if geometry is 2D.

        Args:
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.
            zScale (float): (Optional) The z scale factor.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def setMeasure(self, measureValue: float, measureName: str) -> None:
        """Sets the value of the default measure.

        Or creates the default measure if it doesn't exist. If a 'measureName'
        is supplied, this method sets the value of the named measure, or creates
        the measure if it doesn't exist.

        Args:
            measureValue (float): The measure value.
            measureName (str):  (Optional) The name of the measure whose value
                is to be set, or created.
        """
    def setX(self, newX: float) -> None:
        """Sets the x coordinate of the point.

        Args:
            newX (float): The new x coordinate.
        """
    def setY(self, newY: float) -> None:
        """Sets the y coordinate of the point.

        Args:
            newY (float): The new y coordinate.
        """
    def setZ(self, newZ: float) -> None:
        """Sets the z coordinate of the point.

        Args:
            newZ (float): The new z coordinate.
        """
    def setXYZ(self, newX: float, newY: float, newZ: float) -> None:
        """Sets the xyz coordinates of the point.

        Args:
            newX (float): The new x coordinate.
            newY (float): The new y coordinate.
            newZ (float): (Optional) The new z coordinate.
        """
    def setXYZAsTuple(self, point: tuple[float]) -> None:
        """Set the coordinate value as a tuple.

        The point is forced to 3D if necessary.

        Args:
            point (tuple[float]): The new xyz coordinates.
        """

class FMEMultiPoint(FMEGeometry):
    """FME Multi-Point Class"""

    def __init__(self, multiPoint: FMEMultiPoint) -> None:
        """Creates a Multi-Point geometry from an existing Multi-Point geometry.

        Args:
            multiPoint (FMEMultiPoint): The Multi-Point geometry object to create a copy of.

        Returns:
            (FMEMultiPoint): An instance of a Multi-Point Geometry object.
        """
    def appendPart(self, point: FMEPoint) -> None:
        """This appends the point to the multi point.

        If None is passed in, nothing will be appended. All points in the multi
        point will be forced to have the same dimension. If any 3D points exist,
        all 2D points will be converted to 3D with a default Z value of 0.0.

        Args:
            point (FMEPoint): The point to append.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def appendParts(self, multiPoint: FMEMultiPoint) -> None:
        """This appends the multi point passed in to the multi point.

        If None is passed in, nothing will be appended.

        Args:
            multiPoint (FMEMultiPoint): The multi point to append.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def numParts(self) -> int:
        """Returns the number of parts in the multi point.

        Returns:
          (int): The number of parts in the multi point.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coords specified by 'offsetPoint'.

        Args:
            offsetPoint (FMEPoint): The offset point.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def removeLastPart(self) -> FMEPoint or None:
        """This removes and returns the last point of the multi point.

        If there are no points in the multi point, it will return None.

        Returns:
          (FMEPoint or None): The removed point or None if no parts exist.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def scale(self, xscale: float, yscale: float, zscale: float) -> None:
        """Applies a scale factor to the multi point.

        zscale is ignored if geometry is 2D.

        Args:
            xscale (float): The x scale factor.
            yscale (float): The y scale factor.
            zscale (float): The z scale factor.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """

# Tile Type
FME_TILE_TYPE_FIXED: int
FME_TILE_TYPE_FIXED_MULTIPLE: int
FME_TILE_TYPE_FLEXIBLE: int

# Data Type
FME_DATA_TYPE_NULL: int
FME_DATA_TYPE_REAL64: int
FME_DATA_TYPE_REAL32: int
FME_DATA_TYPE_UINT64: int
FME_DATA_TYPE_INT64: int
FME_DATA_TYPE_UINT32: int
FME_DATA_TYPE_INT32: int
FME_DATA_TYPE_UINT16: int
FME_DATA_TYPE_INT16: int
FME_DATA_TYPE_UINT8: int
FME_DATA_TYPE_INT8: int

class FMERaster(FMEGeometry):
    pass

class FMERasterProperties:
    pass

class FMEBand:
    pass

class FMEBandProperties:
    pass

class FMEPalette:
    pass

class FMETile:
    """FME Tile Class

    FMETile is an abstract class. It cannot be created directly.
    """

    def __init__(self) -> None:
        """Initialze self. See help(type(self)) for accurate signature."""
    def getByteArray(self) -> list[bytearray]:
        """Returns a list of bytearrays where each bytearray represents the data
        values of each row of the tile.

        Returns:
            list[bytearray]: The data values of the tile.
        """
    def getDataAsStringArray(
        self, startRow: int, startCol: int, numRows: int, numCols: int
    ) -> list[str]:
        """Get a list that contains values of the tiles. One string is added to
        the list for each cell in the specified area.

        If the specified area falls outside the bounds of the tile, the string
        array will not be modified. ‘startRow’, ‘startCols’, numRows’, and ‘numCols’
        should be integers greater than or equal to 0.

        Args:
          startRow (int): The starting row.
          startCol (int): The starting column.
          numRows (int): The number of rows.
          numCols (int): The number of columns.

        Returns:
          list[str]: The data as a string array.
        """
    def getDataType(self) -> int:
        """Returns the data type of the raster tile.

        Returns one of:
        - FME_DATA_TYPE_NULL
        - FME_DATA_TYPE_REAL64
        - FME_DATA_TYPE_REAL32
        - FME_DATA_TYPE_UINT64
        - FME_DATA_TYPE_INT64
        - FME_DATA_TYPE_UINT32
        - FME_DATA_TYPE_INT32
        - FME_DATA_TYPE_UINT16
        - FME_DATA_TYPE_INT16
        - FME_DATA_TYPE_UINT8
        - FME_DATA_TYPE_INT8

        Returns:
            int: Data type of a raster tile. For example:
                An FMEInt32Tile would return FME_DATA_TYPE_INT32.
                An FMERGBA64Tile would return FME_DATA_TYPE_UINT16.
                An FMEStringTile would return FME_DATA_TYPE_UINT8.
        """
    def getDataTypeBitDepth(self) -> int:
        """Returns the bit depth of the data type of the raster tile.

        Returns:
            int: The number of bits in the data type of a raster tile. For example:
                An FMEInt32Tile would return 32.
                An FMERGBA64Tile would return 16.
                An FMEStringTile would return 8.
        """
    def getInterpretation(self) -> int:
        """Returns the interpretation of the raster tile.

        Returns one of:
        - FME_INTERPRETATION_NULL
        - FME_INTERPRETATION_REAL64
        - FME_INTERPRETATION_REAL32
        - FME_INTERPRETATION_UINT64
        - FME_INTERPRETATION_INT64
        - FME_INTERPRETATION_UINT32
        - FME_INTERPRETATION_INT32
        - FME_INTERPRETATION_UINT16
        - FME_INTERPRETATION_INT16
        - FME_INTERPRETATION_UINT8
        - FME_INTERPRETATION_INT8
        - FME_INTERPRETATION_GRAY8
        - FME_INTERPRETATION_GRAY16
        - FME_INTERPRETATION_RED8
        - FME_INTERPRETATION_RED16
        - FME_INTERPRETATION_GREEN8
        - FME_INTERPRETATION_GREEN16
        - FME_INTERPRETATION_BLUE8
        - FME_INTERPRETATION_BLUE16
        - FME_INTERPRETATION_ALPHA8
        - FME_INTERPRETATION_ALPHA16
        - FME_INTERPRETATION_NULL
        - FME_INTERPRETATION_RGB24
        - FME_INTERPRETATION_RGBA32
        - FME_INTERPRETATION_RGB48
        - FME_INTERPRETATION_RGBA64
        - FME_INTERPRETATION_STRING

        Returns:
            int: The interpretation of a raster tile. For example:
                An FMERGBA64Tile would return FME_INTERPRETATION_RGBA64.
                An FMERGBA64Tile would return FME_INTERPRETATION_RGBA64.
                An FMEStringTile would return FME_INTERPRETATION_STRING.
        """
    def getInterpretationBitDepth(self) -> int:
        """Returns the bit depth of the interpretation of the raster tile.

        Returns:
            int: The number of bits in the interpretation of a raster tile. For example:
                An FMEInt32Tile would return 32.
                An FMERGBA64Tile would return 64.
                An FMEStringTile would return 8 * stringLength.
        """
    def getInterpretationNumComponents(self) -> int:
        """Returns the number of components in the interpretation of the raster tile.

        Returns:
            int: The number of components in the interpretation of a raster tile. For example:
                An FMEInt32Tile would return 1.
                An FMERGBA64Tile would return 4.
                An FMEStringTile would return 1.
        """
    def getNumCols(self) -> int:
        """Returns the number of columns in the raster tile.

        Returns:
            int: The number of columns in the raster tile.
        """
    def getNumDataTypesPerCell(self) -> int:
        """Returns the number of data types in a cell.

        Returns:
            int: The number of instances of the data type. For example:
              An FMEInt32Tile would return 1.
              An FMERGBA64Tile would return 4.
              An FMEStringTile would return stringLength.
        """
    def getNumRows(self) -> int:
        """Returns the number of rows in the raster tile.

        Returns:
            int: The number of rows in the raster tile.
        """
    def getTileByteLength(self) -> int:
        """Returns the length of the tile in bytes.

        This is equal to numRows * numCols * (interpretationBitDepth / 8)).

        Returns:
            int: The length of the tile in bytes.
        """
    def getTileNumComponents(self) -> int:
        """Returns the number of components in the tile.

        This is equal to numRows * numCols * interpretationNumComponents.

        Returns:
            int: The number of components in the tile.
        """

class FMEAlpha8Tile(FMETile):
    pass

class FMEAlpha16Tile(FMETile):
    pass

class FMEBlue8Tile(FMETile):
    pass

class FMEBlue16Tile(FMETile):
    pass

class FMEGray8Tile(FMETile):
    pass

class FMEGray16Tile(FMETile):
    pass

class FMEGreen8Tile(FMETile):
    pass

class FMEGreen16Tile(FMETile):
    pass

class FMEInt8Tile(FMETile):
    pass

class FMEInt16Tile(FMETile):
    pass

class FMEInt32Tile(FMETile):
    pass

class FMEInt64Tile(FMETile):
    pass

class FMERGB24Tile(FMETile):
    pass

class FMERGB48Tile(FMETile):
    pass

class FMERGBA32Tile(FMETile):
    pass

class FMERGBA64Tile(FMETile):
    pass

class FMEReal32Tile(FMETile):
    pass

class FMEReal64Tile(FMETile):
    pass

class FMERed8Tile(FMETile):
    pass

class FMERed16Tile(FMETile):
    pass

class FMEUInt8Tile(FMETile):
    pass

class FMEUInt16Tile(FMETile):
    pass

class FMEUInt32Tile(FMETile):
    pass

class FMEUInt64Tile(FMETile):
    pass

class FMEStringTileg(FMETile):
    pass

# CSG Solid Operations

FME_CSG_UNION: int
FME_CSG_DIFFERENCE: int
FME_CSG_INTERSECTION: int
FME_CSG_NONE: int

class FMESolidIterator:
    """FME Solid Iterator Class

    FMESolidIterator should not be constructed directly. Instead, use the iterator
    semantics of FMEMultiSolid to get an FMESolidIterator which can be used to
    iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMESimpleSolidIterator:
    """FME Simple Solid Iterator Class

    FMESimpleSolidIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMCompositeSolid to get an FMESimpleSolidIterator which can be
    used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMECSGSolidIterator:
    """FME CSG Solid Iterator Class

    FMECSGSolidIterator should not be constructed directly. Instead, use the iterator
    semantics of FMECSGSolid to get an FMECSGSolidIterator which can be used to
    iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def getOperator(self) -> int:
        """This method returns a valid CSG Boolean Operator if isLeaf() returns True.

        This method returns FME_CSG_NONE if isLeaf() returns False.

        Returns:
            int: Returns a valid CSG Boolean Operator.
        """
    def getPartInLocalCoordinates(self) -> FMESolid or None:
        """This method returns the same solid as next() but if the CSG solid has
        a transformation matrix, the matrix is NOT applied to the leaf solid when
        returned.

        This method must be called after next().

        Returns:
            FMESolid: Returns the solid at the current node in local coordinates.
        """
    def isBranch(self) -> bool:
        """This method returns True if the iterator reaches a branch node in the
        CSG solid tree structure and if next() was called a Stop iteration
        exception would be thrown. This method returns False if the iterator is
        at a leaf node.

        Returns:
            bool: Returns True if the iterator reaches a branch node and false otherwise.
        """
    def isLeftLeaf(self) -> bool:
        """This method returns True if the iterator is at a left leaf node in the
        CSG solid tree structure. This method returns False if the iterator is
        at a branch node.

        Returns:
            bool: Returns True if the iterator is at a left leaf node and false otherwise.
        """
    def isRightLeaf(self) -> bool:
        """This method returns True if the iterator is at a right leaf node in the
        CSG solid tree structure. This method returns False if the iterator is
        at a branch node.

        Returns:
            bool: Returns True if the iterator is at a right leaf node and false otherwise.
        """

class FMESolid(FMEGeometry):
    """FME Solid Class

    FMESolid is an abstract class. It cannot be created directly."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEMultiSolid(FMEGeometry, AppearanceMixin, TransformMixin):
    """FME Multi Solid Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEMultiSolid constructor.

        Returns:
            FMEMultiSolid: An instance of MultiSolid geometry object.
        """
    @overload
    def __init__(self, multiSolid: FMEMultiSolid) -> None:
        """Create a copy of the given multiSolid.

        Returns:
            FMEMultiSolid: An instance of MultiSolid geometry object.
        """
    def appendPart(self, solid: FMESolid) -> None:
        """This appends the MultiSolid passed in to the MultiSolid. If None is
        passed in, nothing will be appended.

        Args:
            solid (FMESolid): A solid to append to the multiSolid.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve or None:
        """Returns the wireframe of the MultiSolid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEMultiCurve: Returns the solid as a wireframe.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getPartAt(self, index: int) -> FMESolid or None:
        """Returns the solid at the given index.

        Args:
            index (int): The index of the solid to return.

        Returns:
            FMESolid: The solid at the given index. Note: This method returns a
                terminal solid type of the FMESolid; i.e. one of the leaf classes
                in the FMESolid inheritance graph. For example, a FMELine is
                returned if the solid truly is a line.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """Returns the number of parts in the MultiSolid.

        Returns:
            int: The number of parts in the MultiSolid.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeLastPart(self) -> FMESolid or None:
        """This removes and returns the last solid of the MultiSolid.

        If there are no solids in the MultiSolid, it will return None.

        Returns:
            FMESolid: The last solid of the MultiSolid. Note: This method returns
                a terminal solid type of the FMESolid; i.e. one of the leaf classes
                in the FMESolid inheritance graph. For example, a FMELine is
                returned if the solid truly is a line.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves parts with default appearances by replacing these
        defaults with the inherited appearance references stored by the parent
        geometry, if such a value exists. The nearest non-default ancestor value
        will be used to set the default appearances on the part.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMESimpleSolid(FMESolid):
    """FME Simple Solid Class

    FMESimpleSolid is an abstract class. It cannot be created directly."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMECompositeSolid(FMESolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME Composite Solid Class"""

    @overload
    def __init__(self) -> None:
        """Default FMECompositeSolid constructor.

        Returns:
            FMEBox: An instance of a Composite Solid geometry object.
        """
    @overload
    def __init__(self, compositeSolid: FMECompositeSolid) -> None:
        """Create a copy of the passed in Composite Solid geometry object.

        Args:
            compositeSolid (FMECompositeSolid): The Composite Solid geometry
                object to create a copy of.

        Returns:
            FMECompositeSolid: Returns:	An instance of a Composite Solid geometry object.
        """
    def appendPart(self, solid: FMESimpleSolid) -> None:
        """Appends a simple solid to the end of this composite solid.

        A None input is ignored.

        Args:
            solid (FMESolid):  The simple solid to be appended.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve or None:
        """Returns the wireframe of the solid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEMultiCurve: The wireframe representation of this solid.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getPartAt(self, index: int) -> FMESimpleSolid or None:
        """Returns the solid at the index specified, or returns None if the index is out of range.

        Returns:
            FMESimpleSolid: The solid at the specified index.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isOriented(self, orientation: int) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """Returns the number of simple solids that are contained in this composite.

        Returns:
            int: The number of parts in the solid.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def orient(self, orientation: int) -> None: ...
    def removeEndPart(self) -> FMESimpleSolid or None:
        """Removes the last simple solid of this composite solid.

        If there are no solids in this composite, this method will return None.

        Returns:
            FMESimpleSolid: The last part of the solid.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves parts with default appearances by replacing these
        defaults with the inherited appearance references stored by the parent
        geometry, if such a value exists. The nearest non-default ancestor value
        will be used to set the default appearences on the part."""
    def reverse(self) -> None: ...
    def rotate2D(self, center: tuple[float], angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEBox(FMESimpleSolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME Box Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEBox constructor.

        Returns:
            FMEBox: An instance of a Box =geometry object.
        """
    @overload
    def __init__(self, coords: tuple[float, float, float, float, float, float]) -> None:
        """Creates a box consisting of the tuple of doubles passed in.

        Args:
            coords: (tuple[double]): The tuple of doubles to set to the box.
                The coords are represented as a tuple of
                (firstX, firstY, firstZ, secondX, secondY, secondZ).

        Returns:
            FMEBox: An instance of a Box Geometry object.
        """
    @overload
    def __init__(
        self,
        coords: tuple[float, float, float, float, float, float],
        matrix: list[list[float]],
    ) -> None:
        """Creates a box consisting of the tuple of doubles passed in.

        With the specified transformation matrix.

        Args:
            coords: (tuple[double]): The tuple of doubles to set to the box.
                The coords are represented as a tuple of
                (firstX, firstY, firstZ, secondX, secondY, secondZ).
            matrix: (tuple[double]): transformation matrix applied to the box,
                formatted [[dddd][dddd][dddd]].

        Returns:
            FMEBox: An instance of a Box Geometry object.
        """
    @overload
    def __init__(self, box: FMEBox) -> None:
        """Creates a box from another box.

        Args:
            box: (FMEBox): The box to copy.

        Returns:
            FMEBox: An instance of a Box Geometry object.
        """
    def getAppearanceReference(self, front: bool) -> int: ...
    def getAsBRepSolid(self) -> FMEBRepSolid:
        """Returns the box as a BRepSolid.

        Returns:
            FMEBRepSolid: The BRepSolid of this box.
        """
    def getAsExtrusion(self) -> FMEExtrusion:
        """Returns the box as an Extrusion.

        Returns:
            FMEExtrusion: The Extrusion representation of this box.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None:
        """Returns the wireframe of the solid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEWireFrame: The wireframe of the solid as a FMEMultiCurve.
        """
    def getCenterPointXYZ(self) -> tuple[float, float, float]:
        """Returns the center point of the box.

        Returns:
            tuple[float,float,float]: A tuple of the center point's x, y and z
                coordinates consecutively, formatted (x, y, z).
        """
    def getLocalFirstPointXYZ(self) -> tuple[float, float, float]:
        """Gets the coordinates of the first point of this box, prior to transformation.

        Returns:
            tuple[float,float,float]: A tuple of the first point's x, y and z
                coordinates consecutively, formatted (x, y, z).
        """
    def getLocalHeight(self) -> float:
        """Gets the height of this box, prior to transformation.

        Returns:
            float: The height of this box.
        """
    def getLocalLength(self) -> float:
        """Gets the length of this box, prior to transformation.

        Returns:
            float: The length of this box.
        """
    def getLocalMaxPoint(self) -> FMEPoint:
        """Gets the maximum point of this box, prior to transformation.

        Returns:
            FMEPoint: The upper point of this box's bounds.
        """
    def getLocalMinPoint(self) -> FMEPoint:
        """Gets the minimum point of this box, prior to transformation.

        Returns:
            FMEPoint: The lower point of this box's bounds.
        """
    def getLocalSecondPointXYZ(self) -> tuple[float, float, float]:
        """Gets the coordinates of the second point of this box, prior to transformation.

        Returns:
            tuple[float,float,float]: A tuple of the second point's x, y and z
                coordinates consecutively, formatted (x, y, z).
        """
    def getLocalSize(self) -> tuple[float, float, float]:
        """Gets the dimensions of this box, prior to transformation.

        The x-, y-, and z-directions correspond to length, width, and height,
        respectively.

        Returns:
            tuple[float,float,float]: A tuple of the box's length, width and height respectively.
        """
    def getLocalWidth(self) -> float:
        """Gets the width of this box, prior to transformation.

        Returns:
            float: The width of this box.
        """
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this box's transformation matrix.

        If the box does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom
        row is always [ 0 0 0 1 ].

        Returns:
            list[list[float]]: The box's tranformation matrix, formatted [[dddd][dddd][dddd]].
        """
    def hasTransformationMatrix(self) -> bool:
        """Returns whether this box has a transformation matrix.

        Returns:
            bool: True if this box has a transformation matrix, False otherwise.
        """
    def isOriented(self, orientation: int) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> FMEBox: ...
    def orient(self, orientation: int) -> FMEBox: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this box's transformation matrix."""
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centerPoint: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setApperanceReference(self, apperanceReference: int, front: bool) -> None: ...
    def setLocalFirstPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the first point of this box, prior to transformation.

        Args:
            x: (float): The x coordinate of the first point.
            y: (float): The y coordinate of the first point.
            z: (float): The z coordinate of the first point.

        Raises:
            FMEException: An exception is raised if an error ocurred.
        """
    def setLocalSecondPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the second point of this box, prior to transformation.

        Args:
            x: (float): The x coordinate of the second point.
            y: (float): The y coordinate of the second point.
            z: (float): The z coordinate of the second point.

        Raises:
            FMEException: An exception is raised if an error ocurred.
        """
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this box's transformation matrix.

        Replacing the existing matrix if it exists. Only three rows are expected
        in the input array, as a bottom row of [ 0 0 0 1 ] is assumed.

        Args:
            matrix: (list[list[float]]): The transformation matrix, formatted [[dddd][dddd][dddd]].
        """

class FMECSGSolid(FMESimpleSolid):
    pass

class FMEExtrusion(FMESimpleSolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME Extrusion Class"""

    @overload
    def __init__(
        self,
        face: FMEFace,
        extrusionVector: tuple[float, float, float],
    ) -> None:
        """Creates an extrusion by a face and extrusion vector.

        Args:
            face: (FMESurface): A face representing the base of the extrusion.
            extrusionVector: (tuple[float,float,float]): The extrusion vector as an (x, y, z) tuple.
        """
    @overload
    def __init__(self, extrusion: FMEExtrusion) -> None:
        """Creates an extrusion by an existing extrusion.

        Args:
            extrusion: (FMEExtrusion): An existing extrusion to copy.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsBRepSolid(self) -> FMEBRepSolid:
        """Returns a boundary-representation solid of this extrusion.

        Returns:
            FMEBRepSolid: The solid as a BRepSolid.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None:
        """Returns the wireframe of the solid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEMultiCurve: The wire-frame representation of this extrusion.
        """
    def getBaseAsFace(self) -> FMEFace:
        """Gets the base of this extrusion solid as a face.

        Returns:
            FMEFace: The base face of this extrusion.
        """
    def getEndCapAsFace(self) -> FMEFace:
        """Gets the end cap of this extrusion solid as a face.

        Returns:
            FMEFace: The end cap face of this extrusion.
        """
    def getExtrusionVectorXYZ(self) -> tuple[float, float, float]:
        """Gets the extrusion vector of this extrusion solid.

        Returns:
            tuple[float,float,float]: The extrusion vector as an (x, y, z) tuple.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isOriented(self, orientation: int) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, orientation: int) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setBase(self, base: FMEFace) -> None:
        """Sets the base of this extrusion solid as the specified face.

        Any existing base that exists in this solid will be replaced. By setting
        the base, the surface normals automatically adjust so that all normals
        are pointing away from the extrusion. If None is passed in, an error will
        result.

        Args:
            base: (FMEFace): The base of the FMEExtrusion as a face.

        Raises:
            FMEException: An exception is raised if an error ocurred.
        """
    def setExtrusionVectorXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the extrusion vector of this extrusion solid.

        Args:
            x: (float): The x-component of the extrusion vector.
            y: (float): The y-component of the extrusion vector.
            z: (float): The z-component of the extrusion vector.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEBRepSolid(FMESimpleSolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME BRepSolid Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of a BRepSolid geometry object"""
    @overload
    def __init__(self, outerSurface: FMESurface) -> None:
        """Creates a new BRepSolid geometry object. The surface passed in is used
        to define the outer surface of the BRepSolid.

        Args:
            outerSurface: (FMESurface): The outer surface as a surface.

        Returns:
            FMEBRepSolid: The new BRepSolid object.
        """
    @overload
    def __init__(self, brepsolid: FMEBRepSolid) -> None:
        """Create a copy of the passed in BRepSolid geometry object.

        Args:
            brepsolid: (FMEBRepSolid): The BRepSolid geometry object to create a copy of.

        Returns:
            FMEBRepSolid: An instance of a BRepSolid Geometry object.
        """
    def addInnerSurface(self, surface: FMESurface) -> None:
        """Adds a new inner surface to the BRepSolid.

        If None is passed in, this solid will not be modified.

        Args:
            surface: (FMESurface): The surface to add to the boundary-representation solid.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def createBRepSolidCopy(self) -> FMEBRepSolid:
        """This routine returns a copy of the given BRepSolid geometry object.

        If there are any errors, an exception is raised.

        Returns:
            FMEBRepSolid: The new BRepSolid object.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireframe(self) -> FMEMultiCurve or None:
        """Returns the outer wireframe of the solid.

        If the solid is not a closed solid, None is returned.

        Returns:
            FMEMultiCurve: The outer wireframe of the solid.
        """
    def getInnerSurfaceAt(self, index: int) -> FMESurface or None:
        """Returns the inner surface at the specified index.

        If the index is out of bounds, None is returned.

        Args:
            index: (int): The index of the inner surface to return.

        Returns:
            FMESurface: The inner surface at the specified index.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getOuterSurface(self) -> FMESurface or None:
        """Returns the outer surface of the solid.

        If the solid is not a closed solid, None is returned.

        Returns:
            FMESurface: The outer surface of the solid.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isOriented(self, orientation: int) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numInnerSurfaces(self) -> int:
        """Returns the number of inner surfaces in the solid.

        Returns:
            int: The number of inner surfaces in the solid.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, orientation: int) -> None: ...
    def removeLastInnerSurface(self) -> FMESurface or None:
        """Removes the last inner surface of this boundary-representation solid.

        If there are no inner surfaces in this solid, this method will return None.

        Returns:
            FMESurface: The last inner surface of the BRepSolid or none.
                Note: This method returns a terminal geometry type of the
                FMESurface; i.e. one of the leaf classes in the FMESurface
                inheritance graph. For example, a FMEFace is returned if the
                geometry truly is a face.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves surface parts with default appearances by replacing
        these defaults with the inherited appearance references stored by the
        parent surface, if such a value exists. The nearest non-default ancestor
        value will be used to set the default appearances on the part."""
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setOuterSurface(self, outerSurface: FMESurface) -> None:
        """Sets the outer surface of this boundary-representation solid as the
        specified FMESurface passed in.

        The outer surface of a boundary-representation solid must exist. Thus,
        if None is passed in, an error will result.

        Args:
            outerSurface: (FMESurface): The outer surface of this solid.

        Raises:
            FMEException: AAn exception is raised if an error occurred, or None is passed in.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMESurface(FMEGeometry, AppearanceMixin, OrientMixin, TransformMixin):
    """FME Surface Class

    FMESurface is an abstract class. It cannot be created directly.
    """

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool:
        """This method deletes the side specified by 'front' and indicates
        whether or not it existed before being deleted.

        Args:
            front (bool): If True then the front side will be deleted, otherwise
                the back side will be deleted.

        Returns:
            (bool): Returns True if the side existed before being deleted and
                returns False if it didn’t exist.
        """
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve or None:
        """Returns the wireframe of the surface as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            (FMEMultiCurve): The wireframe of the surface as a FMEMultiCurve.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane.

        If given normal is the zero vector, the normal used to check the
        planarity is computed using Newell's method as in isPlanar(). valD is a
        reference to a value of D in the plane equation AX + BY + CZ = D. It can
        be used to make sure that multiple pieces lie in the same plane. If
        'recalculateD' is set to False, the passed in value of D will be used in
        the calculation. If 'recalcualted' is set to True, the passed in value
        is ignored and is instead automatically calculated (and returned in the
        second position of the returned tuple). A useful calling pattern for
        ensuring co-planarity is to get valD computed on the first call to the
        function setting 'recalculateD' to True, and then use this value for
        future calls with 'recalculateD' to False.

        Args:
            tolerance (float): The tolerance to check against.
            normalVector (tuple[float,float,float]): The normal used to check
                the planarity.
            valD (float): The value D from 'AX + BY + CZ = D'.
            recalculateD (bool): Whether to recalculate 'D' or not.

        Returns:
            (tuple[bool, tuple, float]): A tuple containing a boolean, tuple, and
            float representing:
            - 1) Whether or not the surface is in plane;
            - 2) The normal vector returned; and
            - 3) The value 'D'. Note: If recalculateD is False, the tuple returned
            will only contain the boolean and vector tuple (i.e. 'valD' is not returned).
        """
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool:
        """Check if this geometry is planar.

        Returns True if this is planar within the given tolerance, and False
        otherwise.

        The planarity condition is computed by the following algorithm. The
        normal vector <A, B, C> is determined by the vertices of this surface
        using Newell's method. For the first point (x', y', z') of this surface,
        we compute D' = Ax' + By' + Cz'. Then, this surface is planar if and
        only if every subsequent point (x, y, z) of this surface gives a
        D = Ax + By + Cz, that is within the tolerance amount of D'. That is,
        | D - D' | <= tolerance.

        If the specified tolerance is negative, then this method always returns True.

        Args:
            tolerence (float): The tolerance to check against.

        Returns:
            (bool): Whether the surface is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool:
        """This method checks whether the side specified by 'front' exists.

        Args:
            front (bool):  If 'front' is true then the front side will be checked
                otherwise the back side will be checked.

        Returns:
            (bool): Returns True if the side exists and False otherwise.
        """

class FMEMultiSurface(FMEGeometry, AppearanceMixin, TransformMixin):
    """FME MultiSurface Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEMultiSurface constructor.

        Returns:
            (FMEMultiSurface): A new instance of the FMEMultiSurface class.
        """
    @overload
    def __init__(self, multiSurface: FMEMultiSurface) -> None:
        """Create a copy of the passed in MultiSurface geometry object.

        Args:
            multiSurface (FMEMultiSurface): The MultiSurface geometry object to
            create a copy of.

        Returns:
            (FMEMultiSurface): A new instance of the FMEMultiSurface class.
        """
    def appendPart(self, surface: FMESurface) -> None:
        """This appends the surface to the MultiSurface.

        If None is passed in, nothing will be appended. All surfaces in the
        MultiSurface will be forced to have the same dimension. If any 3D surfaces
        exist, all 2D surfaces will be converted to 3D with a default Z value of 0.0.

        Args:
            surface (FMESurface): The surface to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendParts(self, multiSurface: FMEMultiSurface) -> None:
        """This appends the MultiSurface passed in to the MultiSurface.

        If None is passed in, nothing will be appended.

        Args:
            multiSurface (FMEMultiSurface): The MultiSurface to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve or None:
        """This method returns a wireframe representation of the MultiSurface.

        Returns:
            (FMEMultiCurve): The wireframe of the contained surfaces or None if
                a multi curve count not be produced.

        Raises:
            FMEException: An exception is raised if there was a failure in
                creating the multi curve Python object.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getPartAt(self, index: int) -> FMESurface or None:
        """This method returns the surface at the specified index.

        None is returned if the index is out of range.

        Args:
            index (int): The index of the surface to return.

        Returns:
            (FMESurface): The surface at the given index. Note: This method returns
            a terminal surface type of the FMESurface; i.e. one of the leaf
            classes in the FMESurface inheritance graph. For example, a FMELine
            is returned if the surface truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane.

        If given normal is the zero vector, the normal used to check the
        planarity is computed using Newell's method as in isPlanar(). valD is a
        reference to a value of D in the plane equation AX + BY + CZ = D. It can
        be used to make sure that multiple pieces lie in the same plane. If
        'recalculateD' is set to False, the passed in value of D will be used in
        the calculation. If 'recalcualted' is set to True, the passed in value
        is ignored and is instead automatically calculated (and returned in the
        second position of the returned tuple). A useful calling pattern for
        ensuring co-planarity is to get valD computed on the first call to the
        function setting 'recalculateD' to True, and then use this value for
        future calls with 'recalculateD' to False.

        Args:
            tolerance (float): The tolerance to check against.
            normalVector (tuple[float,float,float]): The normal used to check
                the planarity.
            valD (float): The value D from 'AX + BY + CZ = D'.
            recalculateD (bool): Whether to recalculate 'D' or not.

        Returns:
            (tuple[bool, tuple, float]): A tuple containing a boolean, tuple, and
            float representing:
            - 1) Whether or not the surface is in plane;
            - 2) The normal vector returned; and
            - 3) The value 'D'. Note: If recalculateD is False, the tuple returned
            will only contain the boolean and vector tuple (i.e. 'valD' is not returned).
        """
    def isPlanar(self, tolerence: float) -> bool:
        """Check if this geometry is planar.

        Returns True if this is planar within the given tolerance, and False
        otherwise.

        The planarity condition is computed by the following algorithm. The
        normal vector <A, B, C> is determined by the vertices of this surface
        using Newell's method. For the first point (x', y', z') of this surface,
        we compute D' = Ax' + By' + Cz'. Then, this surface is planar if and
        only if every subsequent point (x, y, z) of this surface gives a
        D = Ax + By + Cz, that is within the tolerance amount of D'. That is,
        | D - D' | <= tolerance.

        If the specified tolerance is negative, then this method always returns True.

        Args:
            tolerence (float): The tolerance to check against.

        Returns:
            (bool): Whether the surface is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """This method returns the number of parts in this MultiSurface.

        Returns:
            (int): The number of parts in this MultiSurface.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeAppeanceReference(self, front: bool) -> None:
        """When set at this FMEMultiSurface level, the appearance represents the
        default appearance to apply when the contained surfaces use the default
        appearance instead of a specific appearance.

        This call will remove the inherited appearance reference stored at this
        level, if any, on the side specified by the parameter front.

        Args:
            front (bool): Boolean indicting whether the appearance reference
                should be retrieved for the front or back of the multisurface.

        """
    def removeLastPart(self) -> FMESurface or None:
        """This method removes the last part from this MultiSurface.

        Returns:
            (FMESurface): The last surface of the MultiSurface. Note: This method
            returns a terminal surface type of the FMESurface; i.e. one of the leaf
            classes in the FMESurface inheritance graph. For example, a FMELine
            is returned if the surface truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves surface parts with default appearances by replacing
        these defaults with the inherited appearance references stored by the parent
        surface, if such a value exists. The nearest non-default ancestor value
        will be used to set the default appearances on the part.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMECompositeSurface(FMESurface):
    """FME Composite Surface Class"""

    @overload
    def __init__(self) -> None:
        """This method creates a new composite surface.

        Returns:
          (FMECompositeSurface): A new composite surface.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    @overload
    def __init__(self, compositeSurface: FMECompositeSurface) -> None:
        """This method creates a new composite surface.

        Returns:
          (FMECompositeSurface): A new composite surface.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendPart(self, surface: FMESurface) -> None:
        """This method appends a part to this composite surface.

        f None is passed in, nothing will be appended. All areas in the composite
        surface will be forced to have the same dimension. If any 3D areas exist,
        all 2D areas will be converted to 3D with a default Z value of 0.0.

        Args:
            surface (FMESurface): The surface to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool:
        """This method deletes the side specified by 'front' and indicates whether
        or not it existed before being deleted.

        Args:
            front (bool): If True then the front side will be deleted, otherwise
                the back side will be deleted.

        Returns:
            (bool): Whether the side existed before being deleted.
        """
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getPartAt(self, index: int) -> FMESurface: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """This returns the number of surfaces that make up this composite surface.

        Returns:
            (int): The number of surfaces that make up this composite surface.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeEndPart(self) -> FMESurface or None:
        """This method removes the last part from this composite surface.

        If there are no surfaces in the composite surface, it will return None.

        Returns:
            (FMESurface): The last surface of the composite surface. Note: This
                method returns a terminal surface type of the FMESurface;
                i.e. one of the leaf classes in the FMESurface inheritance graph.
                For example, a FMEMesh is returned if the area truly is a mesh.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves surface parts with default appearances by replacing
        these defaults with the inherited appearance references stored by the parent
        surface, if such a value exists.

        The nearest non-default ancestor value will be used to set the default
        appearances on the part."""
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...
    def simpleSurfaceIter(self) -> FMESimpleSurfaceIterator:
        """This creates a simple surface iterator.

        Returns:
          (FMESimpleSurfaceIterator): A simple surface iterator.
        """

class FMESimpleSurface(FMESurface):
    """FME Simple Surface Class

    FMESimpleSurface is an abstract class. It cannot be created directly."""

    def __init__(self) -> None: ...
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...

class FMESimpleSurfaceIterator:
    """FME Simple Surface Iterator Class

    FMESimpleSurfaceIterator should not be constructed directly. Instead, use the
    iterator semantics of FMECompositeSurface to get an FMESimpleSurfaceIterator
    which can be used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class FMEFace(FMESimpleSurface):
    """FME Face Class"""

    @overload
    def __init__(self, boundary: FMEArea, mode: int) -> None:
        """This routine creates a new Face geometry object.

        The stroked boundary of the area is used. If there are any errors,
        None may be returned. If the area passed in is not in 3D, then the
        default value for the z coordinates is 0.0.

        Args:
            boundary (FMEArea): The boundary as an area.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, boundary: FMEArea, mode: int, matrix: list[list[float]]) -> None:
        """This routine creates a new Face geometry object with the specified transformation matrix .

        Args:
            boundary (FMEArea): The boundary as an area.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
            matrix (list[list[float]]):  transformation matrix applied to the face,
                formatted [[dddd][dddd][dddd]].

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, boundary: FMELine, mode: int) -> None:
        """This routine creates a new Face geometry object.

        The stroked boundary of the line is used. If there are any errors,
        None may be returned. If the line passed in is not in 3D, then the
        default value for the z coordinates is 0.0.

        Args:
            boundary (FMELine): The boundary as a line.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, boundary: FMELine, mode: int, matrix: list[list[float]]) -> None:
        """This routine creates a new Face geometry object with the specified transformation matrix .

        Args:
            boundary (FMELine): The boundary as a line.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
            matrix (list[list[float]]):  transformation matrix applied to the face,
                formatted [[dddd][dddd][dddd]].

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, points: list[tuple[float]], mode: int) -> None:
        """Creates a face from the list of points passed in.

        Args:
            points (list[tuple[float]]): The points of the face.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(
        self, points: list[tuple[float]], mode: int, matrix: list[list[float]]
    ) -> None:
        """Creates a face from the list of points passed in with the specified transformation matrix .

        Args:
            points (list[tuple[float]]): The points of the face.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
            matrix (list[list[float]]):  transformation matrix applied to the face,
                formatted [[dddd][dddd][dddd]].

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, face: FMEFace) -> None:
        """Creates a face from the input face.

        Args:
            face (FMEFace): The face.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def addInnerBoundaryCurve(self, innerBoundary: FMECurve, closeMode: int) -> None:
        """Adds an inner-boundary area to this face, represented by the specified curve.

        Refer to setArea() for the usage of the parameter closeMode. If None is
        passed in, this face will not be modified.

        Args:
            innerBoundary (FMECurve): The face's inner boundary as a FMECurve.
            closeMode (int): The close mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def addInnerBoundarySimpleArea(
        self, innerBoundary: FMEArea, closeMode: int
    ) -> None:
        """Adds an inner-boundary area to this face, represented by the specified simple area.

        Args:
            innerBoundary (FMEArea): The face's inner boundary as a FMESimpleArea.
            closeMode (int): The close mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsArea(self) -> FMEArea:
        """Returns the Face as an area.

        Returns:
            (FMEArea): The face as a FMEArea object. Note: This method returns a
            terminal geometry type of the FMEArea; i.e. one of the leaf classes
            in the FMEArea inheritance graph. For example, a FMEPolygon is
            returned if the geometry truly is a polygon.
        """
    def getAsAreaInLocalCoordinates(self) -> FMEArea:
        """Returns the Face as an area in local coordinates.

        Returns:
            (FMEArea): The face as a FMEArea object. Note: This method returns a
            terminal geometry type of the FMEArea; i.e. one of the leaf classes
            in the FMEArea inheritance graph. For example, a FMEPolygon is
            returned if the geometry truly is a polygon.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getNormal(self) -> tuple[float, float, float]:
        """Returns the normal vector of this face, normalized to the unit length.
        The returned vector is computed using Newell's method on the vertices
        contained on the outer boundary of this face. If the face is a single point,
        then a zero vector will be returned.

        Returns:
            (tuple[float,float,float]): The normal vector of this face.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this face's transformation matrix.

        If the face does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom
        row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The face's tranformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTransfromationMatrix(self) -> bool:
        """This method determines if the face has a transformation matrix or not.

        Returns:
            (bool): True if the face has a transformation matrix, False otherwise.
        """
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool:
        """Determines if face is convex.

        The polygon making up the area is convex if all internal angles are less
        than 180 degrees and it's not self-intersecting. Imperfectly planar 3D
        polygons are tolerated.

        Returns:
            (bool): True if the face is convex, False otherwise.
        """
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes the transformation matrix from this face."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setArea(self, area: FMEArea, closeMode: int) -> None:
        """Sets the area of this face.

        The existing area will be replaced and the transformation matrix will be
        reset.The parameter 'closeMode' specifies how this face treates areas
        that are not closed in 3D.

        - If FME_CLOSE_3D_AVERAGE_MODE is specified, an additional point is added,
        connecting the start and end points of the area. This point is computed
        by the average of the start and end points, in 3D.
        - If FME_CLOSE_3D_EXTEND_MODE is specified, the start and end points are
        connected with no additional points.
        - If FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE, we use the AVERAGE mode if
        and only if the start and end points lie on the same coordinate plane
        (i.e. they share the same x-, y-, or z-coordinates).
        - Otherwise, the EXTEND mode is used.
        - If the input area is None, then an error will be generated.

        Args:
            area (FMEArea): The area to set.
            closeMode (int): The face's close mode. Must be either
                FME_CLOSE_3D_AVERAGE_MODE, FME_CLOSE_3D_EXTEND_MODE, or
                FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def setAreaInLocalCoordinates(self, area: FMEArea, closeMode: int) -> None:
        """Sets the area of this face.

        The transformation matrix untouched. Refer to setArea() for the usage of
        the parameter 'closeMode'.

        Args:
            area (FMEArea): The area to set.
            closeMode (int): The face's close mode. Must be either
                FME_CLOSE_3D_AVERAGE_MODE, FME_CLOSE_3D_EXTEND_MODE, or
                FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this face's transformation matrix, replacing the existing matrix
        if it exists. Only three rows are expected in the input array, as a
        bottom row of [ 0 0 0 1 ] is assumed.

        Args:
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
    def sideExists(self, front: bool) -> bool: ...

class FMEFaceIterator(FMESimpleSurface):
    """FME Face Iterator Class

    FMEFaceIterator should not be constructed directly. Instead, use the iterator
    semantics of FMESurface to get an FMEFaceIterator which can be used to
    iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMERectangleFace(FMESimpleSurface):
    """FME Rectangle Face Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of the FMERectangleFace class.

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    @overload
    def __init__(
        self, coordinates: tuple[float, float, float, float, float, float]
    ) -> None:
        """The rectangle has to be parallel to a coordinate plane
        (i.e one of XY, XZ, or YZ plane).

        The first and second points are either the min and max or max and min
        points of the rectangle face. If the first point is the min point, then
        the normal of the rectangle is in the positive direction of the plane it
        is parallel to.

        Arguments:
            coordinates (tuple): tuple of coordinates in form (firstx, firsty,
                firstz, secondx, secondy, secondz).

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    @overload
    def __init__(
        self,
        coordinates: tuple[float, float, float, float, float, float],
        matrix: list[list[float]],
    ) -> None:
        """The rectangle has to be parallel to a coordinate plane
        (i.e one of XY, XZ, or YZ plane).

        The first and second points are either the min and max or max and min
        points of the rectangle face. If the first point is the min point, then
        the normal of the rectangle is in the positive direction of the plane it
        is parallel to.

        Arguments:
            coordinates (tuple): tuple of coordinates in form (firstx, firsty,
                firstz, secondx, secondy, secondz).
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    @overload
    def __init__(self, rectangleFace: FMERectangleFace) -> None:
        """Create a copy of the given rectangle face.

        Arguments:
          rectangleFace (FMERectangleFace): The rectangle face to copy.

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsFaceCopy(self) -> FMEFace:
        """Returns a copy of this face as a FMEFace object.

        Returns:
          (FMEFace): The newly created FMEFace object.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getBoundaryAsLine(self) -> FMELine:
        """Return a copy of this rectangle's boundary as a line.

        Returns:
          (FMELine): The rectangle face's boundary as a line.
        """
    def getLocalFirstPointXYZ(self) -> tuple[float]:
        """Gets the coordinates of the first point of this rectangular face,
        prior to transformation.

        Returns:
          (tuple[float]): The coordinate value of the point.
        """
    def getLocalSecondPointXYZ(self) -> tuple[float]:
        """Gets the coordinates of the second point of this rectangular face,
        prior to transformation.

        Returns:
          (tuple[float]): The coordinate value of the point.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this rectangle face's transformation matrix.

        If the rectangle face does not have such a matrix, an identity matrix is
        returned. Only the top three rows of the matrix will be returned, as the
        bottom row is always [ 0 0 0 1 ]."""
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTransformationMatrix(self) -> bool:
        """This method determines if the rectangle face has a transformation matrix or not.

        Returns:
          (bool): True if this face has a transformation matrix, False otherwise.
        """
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this rectangle face's transformation matrix."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setLocalFirstPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the lower point of this rectangular face,
        prior to transformation.

        Arguments:
          x (float): The x coordinate.
          y (float): The y coordinate.
          z (float): The z coordinate.
        """
    def setLocalSecondPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the upper point of this rectangular face,
        prior to transformation.

        Arguments:
          x (float): The x coordinate.
          y (float): The y coordinate.
          z (float): The z coordinate.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this rectangle face's transformation matrix, replacing the
        existing matrix if it exists.

        Only three rows are expected in the input array, as a bottom row
        of [ 0 0 0 1 ] is assumed.

        Arguments:
          matrix (list[list[float]]): The transformation matrix, formatted
              [[dddd][dddd][dddd]].
        """
    def sideExists(self, front: bool) -> bool: ...

class FMEMesh(FMESimpleSurface):
    """FME Mesh Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEMesh constructor.

        Returns:
            (FMEMesh): An instance of a Mesh geometry object.
        """
    @overload
    def __init__(self, mesh: FMEMesh) -> None:
        """Create a copy of the passed in Mesh geometry object.

        Args:
            mesh (FMEMesh): The Mesh geometry object to create a copy of.

        Returns:
            (FMEMesh): An instance of a Mesh geometry object.
        """
    def addMeshPart(
        self,
        appearanceReference: int,
        vertexIndices: list[int],
        vertexNormalIndices: list[int] or None,
        textureCoordinateIndices: list[int] or None,
    ) -> bool:
        """This routine adds a new mesh part to the mesh.

        The 'vertexNormalIndices' and 'textureCoordinateIndices' may be passed
        in as None if the user does not want to specify vertex normals or
        texture coordinates for the mesh part. The first indices of the mesh
        part should match the respective last indices, indicating a closed face.
        If this is not the case, the mesh part will be closed by the method.

        Args:
            appearanceReference (int): Should refer to a valid appearance in the
                shared object library, but no checking is done during this call.
                The appearance reference of 0 implies that this part will
                inherit the appearance reference of the mesh.
            vertexIndices (list[int]): Should refer to valid vertices in the
                vertex list of the mesh, but no validation is done by the method.
            vertexNormalIndices (list[int] or None): Should refer to valid
                vertex normals stored in the mesh.
            textureCoordinateIndices (list[int] or None): Should refer to valid
                texture coordinates of the mesh.

        Returns:
            (bool): Boolean indicating whether or not the addition was successful.
        """
    def addMeshPartExtended(
        self,
        hasAFront: bool,
        hasABack: bool,
        frontAppRef: int,
        backAppRef: int,
        vertexIndices: list[int],
        vertexNormalIndices: list[int] or None,
        frontTextCoordIndices: list[int] or None,
        backTextCoordIndices: list[int] or None,
    ) -> bool:
        """This routine extends the functionality of addMeshPart(), allowing
        double-sided mesh parts to be added.

        When both 'hasAFront' and 'hasABack' are True, a double sided part will
        be added. If one of these parameters is False, the corresponding
        appearance reference and texture coordinates will not be ignore.

        Args:
            hasAFront (bool): Boolean indicating whether or not the mesh has a front.
            hasABack (bool): Boolean indicating whether or not the mesh has a back.
            frontAppRef (int): Appearance reference for the front of the Mesh.
                Should refer to a valid appearance in the shared object library,
                but no checking is done during this call. The appearance reference
                of 0 implies that this part will inherit the appearance
                reference of the mesh. If 'hasAFront' is False the value of this
                parameter is not important, but it must be a valid int.
            backAppRef (int): Appearance reference for the back of the Mesh.
                Should refer to a valid appearance in the shared object library,
                but no checking is done during this call. The appearance reference
                of 0 implies that this part will inherit the appearance reference
                of the mesh. If 'hasAback' is False the value of this parameter
                is not important, but it must be a valid int.
            vertexIndices (list[int]): Should refer to valid vertices in the
                vertex list of the mesh, but no validation is done by the method.
            vertexNormalIndices (list[int] or None): Should refer to valid vertex
                normals stored in the mesh.
            frontTextCoordIndices (list[int] or None): Should refer to valid
                texture coordinates of the mesh.
            backTextCoordIndices (list[int] or None): Should refer to valid
                texture coordinates of the mesh.

        Returns:
            (bool): Boolean indicating whether or not the addition was successful.
        """
    def appendMesh(self, otherMesh: FMEMesh) -> None:
        """Appends a mesh passed in to the mesh.

        By appending the vertices, vertex normals and texture coordinates and
        then by appending mesh parts with updated indices.

        Args:
            otherMesh (FMEMesh): Another mesh to append to this mesh.
        """
    def appendTextureCoordinate(self, u: float, v: float, w: float, q: float) -> None:
        """Appends the texture coordinate to the end of the texture coordinate list.

        If there are already texture coordinates and a coordinate is supplied
        for a component that doesn't exist, it will be created and back filled
        with math.nan. Parameters set to math.nan will be ignored.

        Args:
            u (float): The U texture coordinate.
            v (float): The V texture coordinate.
            w (float): The W texture coordinate.
            q (float): The Q texture coordinate.
        """
    def appendVertex(self, x: float, y: float, z: float) -> None:
        """Appends the point to the end of the vertex list.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices).

        Args:
            x (float): The X coordinate.
            y (float): The Y coordinate.
            z (float): The Z coordinate.
        """
    def appendVertexColored(
        self, x: float, y: float, z: float, r: float, g: float, b: float
    ) -> None:
        """Appends the point to the end of the vertex list using color information
        provided.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices).

        Args:
            x (float): The x coordinate of the vertex to be appended.
            y (float): The y coordinate of the vertex to be appended.
            z (float): The z coordinate of the vertex to be appended.
            r (float): The r value of the color.
            g (float): The g value of the color.
            b (float): The b value of the color.
        """
    def appendVertexNormal(self, x: float, y: float, z: float) -> None:
        """Appends the point to the end of the vertex normal list.

        Args:
            x (float): The x coordinate of the vertex to be appended.
            y (float): The y coordinate of the vertex to be appended.
            z (float): The z coordinate of the vertex to be appended.
        """
    def appendVertexNormals(self, points: list[tuple[float]]) -> None:
        """Appends the vertex normals to the end of the vertex normal list.

        Args:
            points (list[tuple[float]]): The list of vertices to be added.
                The vertices are represented as (x, y, z) tuples.
        """
    def appendVertices(self, points: list[tuple[float]]) -> None:
        """Appends the vertices to the end of the vertex list.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices).

        Args:
            points (list[tuple[float]]): The list of vertices to be added.
                The vertices are represented as (x, y, z) tuples.
        """
    def appendVerticesColored(
        self, pointsColorsAndHasColor: list[tuple[float, bool]]
    ) -> None:
        """Appends the vertices to the end of the vertex list using color
        information provided.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices). The
        hasColor flag specifies whether a valid color exists at that vertex index.

        Args:
            pointsColorsAndHasColor (list[tuple[float, bool]]): The list of
                tuple of vertices, colors, and has color flag to be added. A
                tuple is in the form (x, y, z, r, g, b, hasColor), where
                vertices are the x, y, z as floats, color components are r, g, b
                as floats, and the hasColor is a bool.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self,
        destFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsCompositeSurface(self) -> FMECompositeSurface or None:
        """Returns a composite surface representation of this mesh.

        None is returned when an error is encountered.

        Returns:
            (FMECompositeSurface or None): Returns a composite surface
                representation of this mesh or none.
        """
    def getAsMultiSurface(self) -> FMEMultiSurface or None:
        """Returns a multi-surface representation of this mesh.

        None is returned when an error is encountered.

        Returns:
            (FMEMultiSurface or None): Returns a multi-surface representation
                of this mesh or none.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type or None: ...
    def getTextureCoordinateAt(self, index: int) -> tuple[float] or None:
        """Retrieve the texture coordinate at the specified index.

        Only components of the texture coordinate that return True from
        hasTextureCoordinates[U|V|W|Q] will be fetched. A value of None means
        that the texture coordinate value doesn't exist at that index. An error
        is returned if the index is out of range.

        Args:
            index (int): The index of the texture coordinate to retrieve.

        Returns:
            (tuple[float] or None): The texture coordinate at the specified
                index.

        Raises:
            FMEException: An error occurred.
        """
    def getTextureCoordinates(self) -> list[tuple[float]]:
        """Retrieves the texture coordinate list with texture coordinates in the
        same index position as referenced by the faces.

        Only components where hasTextureCoordinates[U|V|W|Q] is true will be
        fetched.

        Returns:
            (list[tuple[float]]): The list of coordinates represented as
                (u, v, w, q) tuples.
        """
    def getTrait(
        self,
        traitName: str,
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this mesh's transformation matrix.

        If the mesh does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom
        row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The mesh's tranformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
    def getVertexAt(self, index: int) -> tuple[float] or None:
        """Retrieve the vertex, in global coordinates

        (i.e., the transformation matrix is applied, if it exists), at the
        specified index. An FMEException is raised if the index is out of range.

        Args:
            index (int): The index of the vertex to retrieve.

        Returns:
            (tuple[float] or None):The vertex at the index represented as a
                (x, y, z) tuple.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexColorAt(self, index: int) -> tuple[float] or None:
        """Retrieves the vertex color at the specified index.

        Raises an FMEException when a valid color does not exist at the
        specified index, the index is out of range, or the mesh does not contain
        vertex colors.

        Args:
            index (int): The index of the vertex color to retrieve.

        Returns:
            (tuple[float] or None): The vertex at the index represented as a
                (x, y, z) tuple.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexNormalAt(self, index: int) -> list[tuple[float]]:
        """Retrieve the vertex normal, in global coordinates

        (i.e., the transformation matrix is applied, if it exists), at the
        specified index. An FMEException is raised if the index is out of range.

        Args:
            index (int): The index of the vertex normal to retrieve.

        Returns:
            (list[tuple[float]]): The vertex normal at the index represented as
                a (x, y, z) tuple.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexNormals(self) -> list[list[float]]:
        """Retrieves the vertex normal list with vertex normals, in global
        coordinates

        (i.e., the transformation matrix is applied, if it exists), in the same
        index position as referenced by the faces.

        Returns:
            (list[list[float]]): The list of vertex normals represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexNormalsInLocalCoordinates(self) -> list[list[float]]:
        """This is the same as getVertexNormals() with the exception that the
        transformation matrix is not applied.

        Returns:
            (list[list[float]]): The list of vertex normals represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def getVertices(self) -> list[tuple[float]]:
        """Retrieves the vertex list with vertices, in global coordinates

        (i.e., the transformation matrix is applied, if it exists), in the same
        index position as referenced by the faces.

        Returns:
            (list[tuple[float]]): The list of vertices represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def getVerticesInLocalCoordinates(self) -> list[tuple[float]]:
        """This is the same as getVertices() with the exception that the
        transformation matrix is not applied.

        Returns:
            (list[tuple[float]]): The list of vertices represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def hasColorAtVertex(self, index: int) -> bool:
        """This method determines if there is color at a vertex.

        Args:
            index (int): The index of the vertex color to check.

        Returns:
            (bool): Returns True if a valid color exists at the specified index,
                otherwise returns False if a valid color does not exist at the
                specified index, the index is out of range, or the mesh does not
                contain vertex colors.
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTextureCoordinatesQ(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTextureCoordinatesU(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTextureCoordinatesV(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTextureCoordinatesW(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTransformationMatrix(self) -> bool:
        """This method determines if the mesh has a transformation matrix or not.

        Returns:
            (bool): True if this geometry has a transformation matrix, False
                otherwise.
        """
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valId: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def maxEdgeNumber(self) -> int:
        """Returns the maximum number of edges the mesh can contain.

        Returns:
            (int): The maximum number of edges in this geometry.
        """
    def measureExists(self, measureName: str) -> bool:
        """CReturns True if the specified measure exists and False otherwise.

        If the 'measureName' parameter is not specified then the default measure
        is checked.

        Returns:
            (bool): Boolean indicating whether or not the measure exists.
        """
    def numParts(self) -> int:
        """This returns the number of faces that are contained in this geometry.

        Returns:
            (int): The number of parts in this geometry.
        """
    def numTextureCoordinates(self) -> int:
        """Returns the number of texture coordinates that are contained in this mesh.

        Returns:
            (int): Returns the number of texture coordinates that are contained
                in this mesh.
        """
    def numVertexColors(self) -> int:
        """Returns the total number of vertex colors, including invalid ones.

        This will be either 0, if the mesh does not contain vertex colors, or
        the same as the number of vertices.

        Returns:
            (int): Returns the number of vertex colors.
        """
    def numVertexNormals(self) -> int:
        """Returns the number of vertex normals that are contained in this mesh.

        Returns:
            (int): Returns the number of vertex normals in this mesh.
        """
    def numVertexNormalsInLocalCoordinates(self) -> int:
        """This is the same as numVertexNormals() with the exception that the
        transformation matrix is not considered.

        If the transformation matrix is not invertible, this will return the
        number of unmodified normals, numVertexNormals() will return 0 because
        the normals will be removed if a non-invertible matrix is applied.

        Returns:
            (int): Returns the number of vertex normals in local coordinates for this mesh.
        """
    def numVertices(self) -> int:
        """Returns the number of vertices that are contained in this mesh.

        Returns:
            (int): Returns the number of vertices in this mesh.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def optimizeVertexPool(self) -> None:
        """Optimizes the mesh by removing all duplicate and unreferenced vertices,
        vertex normals, and texture coordinates.

        This will modify the underlying vertex pools and update the mesh part
        indices. This is a potentially expensive operation and should not be
        called unless necessary.
        """
    def orient(self) -> None: ...
    def removeDegenerateTriangleMeshParts(self) -> None:
        """Removes this mesh's degenerate triangle parts."""
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this mesh's transformation matrix."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resetGeometry(self) -> None:
        """Removes all vertices, texture coordinates, normals, and mesh parts."""
    def resolvePartDefaults(self) -> bool:
        """This call assumes that the mesh has been triangulated.

        It will remove any mesh parts that do not have three edges and will also
        remove triangles with repeated vertex indices. It will return true if
        any parts are removed by the call. This method assumes that duplicate
        indices have already been removed from the mesh.

        Returns:
            (bool): Returns True if any parts are removed by the call and False
                otherwise.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setEdgeVisibilityFlagsToLastPart(
        self,
        edgeVisibilityFlags: list[bool],
    ) -> None:
        """This routine sets the edge visibility flags to the last mesh part
        that was added.

        It is intended to be called directly after addMeshPart(),
        typically. The size of the list of flags must be exactly one fewer than
        the number of vertices on the last part of the mesh.

        Passing in None will remove all edge visibility flags from the last mesh
        part.

        Args:
            edgeVisibilityFlags (list[bool]): The list of edge visibility flags.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this mesh's transformation matrix, replacing the existing matrix if it exists.

        Only three rows are expected in the input array, as a bottom row of
        [ 0 0 0 1 ] is assumed.

        Args:
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
    def sideExists(self, front: bool) -> bool: ...

class FMEMeshPartIterator:
    """FME Mesh Part Iterator Class

    FMEMeshPartIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMesh to get an FMEMeshPartIterator which can be
    used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def getAppearanceReference(self, front: bool) -> int:
        """This method returns the appearance reference within the Library associated with this mesh part iterator. T

        The front parameter controls whether this query should return the front
        or the back appearance reference. Both can be fetched independently. If
        this mesh part iterator is a regular mesh part iterator with no geometry
        instance, a FMEException will be thrown.

        Args:
            front (bool): If True, the front appearance reference is returned.
                If False, the back appearance reference is returned.

        Returns:
            (int): The appearance reference for the geometry.

        Raises:
            FMEException: An exception is raised if this mesh part iterator is
            not associated with a geometry instance.
        """
    def getTextureCoordinateIndices(self, front: bool) -> list[int] or None:
        """This method returns the texture coordinate indices associated with this mesh part iterator.

        The front parameter controls whether this query should return the front
        or the back texture coordinate indices. Both can be fetched independently.

        Args:
            front (bool): Indicates whether the indices should be fetched for
                the front or back of the mesh part.

        Returns:
            (list[int]): The texture coordinate indices or None if a problem occurred.
        """
    def getVertexIndices(self) -> list[int] or None:
        """Returns the vertex indices in the current mesh part via a list of ints.

        Returns:
            (list[int]): The vertex indices or None if a problem occurred.
        """
    def getVertexNormalIndices(self) -> list[int] or None:
        """Returns the vertex normal indices in the current mesh part via a list of ints.

        Returns:
            (list[int]): The vertex normal indices or None if a problem occurred.
        """
    def hasTextureCoords(self, front: bool) -> bool:
        """Returns a boolean indicating whether or not the mesh part iterator has texture coordinates.

        The front parameter controls whether this query should be made on the
        front or back of the mesh part.

        Args:
            front (bool): Indicates whether the indices should be fetched for
                the front or back of the mesh part.

        Returns:
            (bool): True if the mesh part has texture coordinates, False otherwise.
        """
    def hasVertexNormals(self) -> bool:
        """Returns a boolean indicating whether or not the mesh part iterator has vertex normals.

        Returns:
            (bool): True if the mesh part has vertex normals, False otherwise.
        """
    def numVertices(self) -> int:
        """Returns the number of vertices.

        Returns:
            (int): The number of vertices.
        """
    def seek(self, index: int) -> bool:
        """This method advances the iterator to the mesh part specified by index,
        if it exists.

        Returns true if there is a valid part at the index and false if there is not.

        Args:
            index (int): The index to advance the iterator to.

        Returns:
            (bool): Indicates whether or not the mesh part at index is a valid part.
        """
    def sideExists(self, front: bool) -> bool:
        """Indicates whether of not the side of the mesh part exists.

        The front parameter controls whether this query should be made on the
        front or back of the mesh part.

        Args:
            front (bool):Indicates whether the query should be made on thhe
                front or back of the mesh part.

        Returns:
            (bool): Returns True if th side exists or False otherwise.
        """

class FMETriangleFan(FMESimpleSurface):
    """FME Triangle Fan Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of a Triangle Fan geometry object.

        Returns:
          (FMETriangleFan): An instance of a Triangle Fan geometry object.
        """
    @overload
    def __init__(self, points: list[tuple[float]]) -> None:
        """Creates a line consisting of the list of points.

        Args:
          points (list): The list of points to set to the triangle fan. The points are represented as (x, y, z) tuples.

        Returns:
          (FMETriangleFan): An instance of a Triangle Fan geometry object.
        """
    @overload
    def __init__(self, triangleFan: FMETriangleFan) -> None:
        """Creates a triangle fan from another triangle fan.

        Args:
          triangleFan (FMETriangleFan): The triangle fan to copy.

        Returns:
          (FMETriangleFan): An instance of a Triangle Fan geometry object.
        """
    def appendPointXYZ(self, x: float, y: float, z: float) -> None:
        """Appends coordinates to the end of the coordinate list that defines the
        triangle fan.

        This operation effectively appends new triangles to the triangle fan.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          x (float): The x coordinate of the point.
          y (float): The y coordinate of the point.
          z (float): The z coordinate of the point.
        """
    def appendPoints(self, points: list[tuple[float]]) -> None:
        """Appends coordinates to the end of the coordinate list that defines the
        triangle fan.

        This operation effectively appends new triangles to the triangle fan.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          points (list): The list of points to set to the triangle fan.
              The points are represented as (x, y, z) tuples.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsFaceAt(self, index: int) -> FMEFace or None:
        """Returns a triangular face defined by this triangle fan.

        The index indicates the specific triangular face to return. In particular,
        given an index i, the triangular face returned is specified by the
        coordinate indices 0, i + 1, and i + 2. If the specified index is out of
        range, then None is returned.

        Args:
          index (int): The index of the face to return.

        Returns:
          (FMEFace): A copy of a triangular face defined by this triangle fan.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValueAt(self, index: int, measureName: str) -> float:
        """Get the value of the default measure at the 'index'.

        If 'measureName' is supplied, this method gets the value of the named
        measure at 'index'. Returns an error if the measure doesn't exist or
        'index' is out of range.

        Args:
          index (int): The index of the measure to return.
          measureName (str): (optional) The name of the measure to return.

        Returns:
          (float): The value of the default measure at the given index, or the
              measure named by 'measureName' at the given index.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getMeasureValues(self, measureName: str) -> list[float]:
        """Returns the value of the default measure, or the value of the measure
        named by 'measureName'.

        Args:
          measureName (str): (optional) The name of the measure to return.

        Returns:
          (list[float]): The values of the default measure, or the measures named
              by 'measureName'.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getName(self) -> text_type or None: ...
    def getPointAtXYZ(self, index: int) -> tuple[float]:
        """Gets a coordinate of this triangle fan at the specified index.

        If index is out of range, then an error is generated.

        Args:
          index (int): The index of the coordinate to return.

        Returns:
          (tuple[float]): The point is represented as a (x, y, z) tuple.

        Raise:
          FMEException: An exception is raised if an error occurred
        """
    def getPoints(self) -> list[FMEPoint]:
        """Gets the points of the triangle fan as a list of FMEPoint objects.
        The size of the given list must be exactly equal to the value returned
        by numPoints(). If the triangle fan is 2D the z values of the triangle
        fan will be populated with 0.0 values. Returns an error if an error occurred.

        Returns:
          (list[FMEPoint]): A list of points contained within the triangle fan.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getPointsAsLine(self) -> FMELine:
        """Returns a line that contains the points in this triangle fan.

        The line will have all the geometry traits and measures of the triangle fan.

        Returns:
          (FMELine): A copy of a line that contains the points in this triangle fan.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def numPoints(self) -> int:
        """Returns the number of coordinates in the triangle fan.

        Returns:
          (int): The number of coordinates in the triangle fan.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, front: bool, appearanceReference: int) -> None: ...
    def setMeasure(self, measureValues: list[float], measureName: str) -> None:
        """Set the default measure to the given values.

        Create the measure if it doesn't already exist. If 'measureName' is
        supplied, this method sets the given measure to 'measureValues', or
        creates the measure if it doesn't already exist. The size of 'measureValues'
        must be exactly equal to the value returned by numPoints().

        Args:
          measureValues (list[float]): The values to set.
          measureName (str): Optional) The name of the measure whose value is to
          be set, or created.
        """
    def setMeasureAt(
        self, index: int, measureValues: list[float], measureName: str
    ) -> None:
        """Set the default measure of the point at 'index' to the given 'measureValue'.

        If 'measureName' is supplied, this method sets the given measure of the
        point at 'index' to 'measureValue'. Creates the measure if it doesn't
        already exist and set the measures to all points other than the point at
        the given index to None. Return an error if the index is out of range.

        Args:
          index (int): The index of the measure to set.
          measureValues (list[float]): The values to set.
          measureName (str): Optional) The name of the measure whose value is to
          be set, or created.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...

class FMETriangleStrip(FMESimpleSurface):
    """FME Triangle Strip Class"""

    @overload
    def __init__(self) -> None:
        """Create and instance of the FMETriangleStrip class.

        Returns:
          (FMETriangleStrip): An instance of the FMETriangleStrip class.
        """
    @overload
    def __init__(self, points: list[tuple[float]]) -> None:
        """Creates a line consisting of the list of points passed in.

        Args:
          points (list[tuple[float]]): The list of points to set to the triangle
              strip. The points are represented as (x, y, z) tuples.

        Returns:
          (FMETriangleStrip): An instance of the FMETriangleStrip class.
        """
    @overload
    def __init__(self, triangleStrip: FMETriangleStrip) -> None:
        """Creates a copy of the given triangle strip.

        Args:
          triangleStrip (FMETriangleStrip): The triangle strip to copy.

        Returns:
          (FMETriangleStrip): An instance of the FMETriangleStrip class.
        """
    def appendPointXYZ(self, x: float, y: float, z: float) -> None:
        """Appends coordinates to the end of the coordinate list that defines the triangle strip.

        This operation effectively appends new triangles to the triangle strip.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          x (float): The x value of the point to append.
          y (float): The y value of the point to append.
          z (float): The z value of the point to append.
        """
    def appendPoints(self, points: list[tuple[float]]) -> None:
        """Appends coordinates to the end of the coordinate list that defines the triangle strip.

        This operation effectively appends new triangles to the triangle strip.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          points (list[tuple[float]]): The list of points to append. The points
              are represented as (x, y, z) tuples.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsFaceAt(self, index: int) -> FMEFace or None:
        """Returns the face at the given index.

        Args:
          index (int): The index of the face to return.

        Returns:
          (FMEFace): A copy of a triangular face defined by this triangle strip.
        """
    def getAsWireFrame(self) -> FMEMultiCurve or None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValueAt(self, index: int, measureName: str) -> float:
        """Get the value of the default measure at the 'index'.

        If 'measureName' is supplied, this method gets the value of the named
        measure at 'index'. Returns an error if the measure doesn't exist or
        'index' is out of range.

        Args:
          index (int): The index of the measure to return.
          measureName (str): (Optional) The name of the measure whose value is
              to be returned.

        Returns:
          (float): The value of the default measure at the given index, or the
          measure named by 'measureName' at the given index.
        """
    def getMeasureValues(self, measureName: str) -> list[float]:
        """Get the values of the default measureor the value of the measure named by 'measureName'.

        Args:
          measureName (str): (Optional) The name of the measure whose value is
              to be returned.

        Returns:
          (list[float]): The values of the default measure, or the measures named by 'measureName'.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getName(self) -> text_type or None: ...
    def getPointAtXYZ(self, index: int) -> tuple[float]:
        """Gets a coordinate of this triangle strip at the specified index.

        If index is out of range, then an error is generated.

        Args:
          index (int): The index of the point to return.

        Returns:
          (tuple[float]): The point at the given index.
        """
    def getPoints(self) -> list[FMEPoint]:
        """Gets the points of the triangle strip as a list of FMEPoint objects.

        The size of the given list must be exactly equal to the value returned
        by numPoints(). If the triangle strip is 2D the z values of the triangle
        strip will be populated with 0.0 values. Throws an exception if an error
        occurred.

        Returns:
          (list[FMEPoint]): The points of this triangle strip.

        Raise:
          FMEException: An exception is raised if an error occurred
        """
    def getPointsAsLine(self) -> FMELine:
        """Returns a line that contains the points in this triangle strip.

        The line will have all the geometry traits and measures of the triangle strip.

        Returns:
          (FMELine): A copy of a line that contains the points in this triangle strip.
        """
    def getTrait(
        self, traitName: str
    ) -> bool or int or float or string_types or bytearray or bytes or None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isFlipped(self) -> bool:
        """Determines whether the orientation of the triangle strip is the opposite
        of what the first triangle indicates (using a right-handed coordinate system).

        Returns:
          (bool): Returns True if the orientation of the triangle strip is the
              opposite of what the first triangle indictes and False otherwise.
        """
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def numPoints(self) -> int:
        """Gets the number of points in this triangle strip.

        Returns:
          (int): The number of points in this triangle strip.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setMeasure(self, measureValues: list[float], measureName: str) -> None:
        """Sets the default measure of this triangle strip to the given values.

        Create the measure if it doesn't already exist. If 'measureName' is supplied,
        this method sets the given measure to 'measureValues', or creates the
        measure if it doesn't already exist. The size of 'measureValues' must be
        exactly equal to the value returned by numPoints().

        Args:
          measureValues (list[float]): The values of the default measure.
          measureName (str): (Optional) The name of the measure whose value is to
              be set, or created.
        """
    def setMeasureAt(self, index: int, measureValue: float, measureName: str) -> None:
        """Sets the value of the default measure at the 'index'.

        If 'measureName' is supplied, this method sets the given measure of the
        point at 'index' to 'measureValue'. Creates the measure if it doesn't
        already exist and set the measures to all points other than the point at
        the given index to None. Return an error if the index is out of range.

         Args:
           index (int): The index of the measure to set.
           measureValue (float): The value of the measure to set.
           measureName (str): (Optional) The name of the measure whose value is
              to be set, or created.

         Raises:
           FMEException: An exception is raised if an error occurred
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool or int or float or text_type or bytearray or bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...

class FMETextIterator:
    """FME Text Iterator Class

    FMETextIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMultiText to get an FMETextIterator which can be
    used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEText(FMEGeometry):
    """FME Text Class"""

    @overload
    def __init__(
        self,
        location: FMEGeometry,
        textString: text_type,
        textSize: float,
        textRotation: float,
    ) -> None:
        """Creates a new Text geometry object.

        'textRotation' is CCW up from the horizontal and is measured in degrees.
        'textSize' is the height of the text's box before rotation. It includes
        all lines and interline spacing for multi-line text. The 'textString' is
        specified as a six.text_type , which is set as an encoded text string on
        the text object.

        Args:
            location (FMEGeometry): The location of the text.
            textString (text_type): The text string to display.
            textSize (float): The text size.
            textRotation (float): The rotation value to set.

        Returns:
            (FMEText): An instance of a Text Geometry object.
        """
    @overload
    def __init__(self, text: FMEText) -> None:
        """Creates a text from an existing text.

        Args:
            text (FMEText): The Text geometry object to create a copy of.

        Returns:
            (FMEText): An instance of a Text Geometry object.
        """
    def getLocation(self, asPoint: bool) -> FMEGeometry or FMEPoint:
        """Returns the location of the text.

        Args:
            asPoint (bool): Whether to return the location as a FMEPoint

        Returns:
            (FMEGeometry): The location of the text.
        """
    def getTextRotation(self) -> float:
        """Returns the rotation of the text object.

        The returned rotation is counter-clockwise up from the horizontal and is
        measured in degrees.

        Returns:
            (float): The text rotation.
        """
    def getTextSize(self) -> float:
        """Returns the text size of the text object.

        Text size is actually the height of hte text's box before rotation. It
        includes all lines and interline spacing for multiline text.

        Returns:
            (float): The text size.
        """
    def getTextString(self) -> text_type:
        """Returns the text string of the text object.

        It includes all lines and interline spacing for multi-line text.

        Returns:
            (text_type): The text string.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coordinate values specified by 'offsetPoint'.

        An error is returned if the operation is unsuccessful.

        Args:
            offsetPoint (FMEPoint): The point whose coordinate values will be
                used to offset the text object.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def reset(self, text: FMEText) -> None:
        """Resets the existing text object, and sets its values to the data stored
        in 'text'.

        Args:
            text (FMEText): The FMEText object whose data will be set to the
                existing text object.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates the text counterclockwise around the 'center' point by the
        specified 'angle' (in degrees). An error is returned if the operation is
        unsucessful.

        Args:
            center (FMEPoint): The center point around which the text will be rotated.
            angle (float): The angle of rotation in degrees.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def scale(
        self, xScale: float, yScale: float, zScale: float, scaleText: bool
    ) -> None:
        """Scale the feature by the given amounts.

        'zScale' is ignored if the text object is 2D. An error is returned if
        the operation is unsucessful.

        Args:
            xScale (float): The x-scale factor.
            yScale (float): The y-scale factor.
            zScale (float): The z-scale factor.
            scaleText (bool): (Optional) Whether to scale the text.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def setLocation(self, location: FMEGeometry) -> None:
        """Sets the existing text object's location to the value in 'location.
        An error is returned if the new location is invalid or NULL.

        Args:
            location (FMEGeometry): The new location of the text.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def setTextRotation(self, textRotation: float) -> None:
        """Sets the rotation of the text object.

        The rotation is counter-clockwise up from the horizontal and is
        measured in degrees.

        Args:
            textRotation (float): The text rotation.
        """
    def setTextSize(self, textSize: float) -> None:
        """Sets the text size of the text object.

        An error is returned if the new size is invalid or NULL.

        Args:
            textSize (float): The text size.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setTextString(self, textString: text_type) -> None:
        """Sets the existing text object's text string to 'textString'.

        The 'textString' is specified as a six.text_type, which is set as an
        encoded text string on the text object.

        Args:
            textString (text_type): The text string.
        """

class FMEMultiText(FMEGeometry):
    """FME Multi-Text Class"""

    def __init__(self, multiText: FMEMultiText) -> None:
        """Creates a new Multi-Text object from an existing Multi-Text object.

        Args:
            multiText (FMEMultiText): The Multi-Text object to create a copy of.

        Returns:
            (FMEMultiText): An instance of a Multi-Text Geometry object.
        """
    def appendPart(self, text: FMEText) -> None:
        """This appends the text to the existing MultiText.

        If None is passed in, nothing will be appended. All texts in the
        MultiText will be forced to have the same dimension. If any 3D texts
        exist, all 2D texts will be converted to 3D with a default Z value of 0.0.

        Args:
            text (FMEText): The text to append.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def appendParts(self, multiText: FMEMultiText) -> None:
        """This appends the texts to the existing MultiText.

        If None is passed in, nothing will be appended.

        Args:
            multiText (FMEMultiText): The MultiText to append.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def getPartAt(self, index: int) -> FMEText or None:
        """Returns the text at the specified index.

        Args:
            index (int): The index of the text to return.

        Returns:
            (FMEText): The text at the given index. Note: This method returns a
                terminal text type of the FMEText ; i.e. one of the leaf classes
                in the FMEText inheritance graph. For example, a FMELine is
                returned if the text truly is a line.
        """
    def numParts(self) -> int:
        """Returns the number of parts in the MultiText.

        Returns:
            (int): The number of parts.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coordinate values specified by 'offsetPoint'.

        An error is returned if the operation is unsuccessful.

        Args:
            offsetPoint (FMEPoint): The point whose coordinate values will be
                used to offset the text object.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def removeLastPart(self) -> FMEText or None:
        """This removes and returns the last text of the MultiText.

        If there are no texts in the MultiText, it will return None.

        Returns:
            (FMEText): The last text of the MultiText. Note: This method returns
                a terminal text type of the FMEText; i.e. one of the leaf classes
                in the FMEText inheritance graph. For example, a FMELine is
                returned if the text truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """The angle is CCW up from the horizontal and is measured in degrees.

        Args:
            centre (FMEPoint): The center point around which the text will be rotated.
            angle (float): The angle of rotation in degrees.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def scaleXYZ(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scale the feature by the given amounts.

        'zScale' is ignored if the text object is 2D. An error is returned if
        the operation is unsucessful.

        Args:
            xScale (float): The x-scale factor.
            yScale (float): The y-scale factor.
            zScale (float): The z-scale factor.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def scaleXYZT(
        self, xScale: float, yScale: float, zScale: float, scaleText: bool
    ) -> None:
        """Scale the feature by the given amounts.

        'zScale' is ignored if the text object is 2D. An error is returned if
        the operation is unsucessful.

        Args:
            xScale (float): The x-scale factor.
            yScale (float): The y-scale factor.
            zScale (float): The z-scale factor.
            scaleText (bool): (Optional) Whether to scale the text.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """

class FMEReprojector:
    pass

class FMECoordSysManager:
    pass

# Closing Curves in 3D
FME_CLOSE_3D_AVERAGE_MODE: int
FME_CLOSE_3D_EXTEND_MODE: int
FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE: int

# Calculating Vertex Normals
BY_FACE: int

# Refine Area Type
FME_RA_PATH_CONCAT_LINES: int
FME_RA_PATH_EXTRACT_SINGLE_LINES: int
FME_RA_PATH_EXTRACT_SINGLE_ARCS: int
FME_RA_ARC_STANDARDIZE: int
FME_RA_ARC_STROKE: int
FME_RA_AREA_STANDARDIZE: int
FME_RA_LINE_REMOVE_DUPLICATE_COORDS: int
FME_RA_LINE_REMOVE_DUPLICATE_COORDS_Z: int

# Refine Curve Type
FME_RC_PATH_CONCAT_LINES: int
FME_RC_PATH_EXTRACT_SINGLE_LINES: int
FME_RC_PATH_EXTRACT_SINGLE_ARCS: int
FME_RC_ARC_STANDARDIZE: int
FME_RC_ARC_STROKE: int
FME_RC_LINE_REMOVE_DUPLICATE_COORDS: int
FME_RC_LINE_REMOVE_DUPLICATE_COORDS_Z: int

# Refine Geometry Type
FME_RG_PATH_CONCAT_LINES: int
FME_RG_PATH_EXTRACT_SINGLE_LINES: int
FME_RG_PATH_EXTRACT_SINGLE_ARCS: int
FME_RG_ARC_STANDARDIZE: int
FME_RG_ARC_STROKE: int
FME_RG_AREA_STANDARDIZE: int
FME_RG_LINE_REMOVE_DUPLICATE_COORDS: int
FME_RG_LINE_REMOVE_DUPLICATE_COORDS_Z: int
FME_RG_AGG_OR_MULTI_EXTRACT_SINGLETONS: int
FME_RG_AGG_OR_MULTI_RECURSE: int
FME_RG_AGG_CONVERT_HOMOGENEOUS_TO_MULTI: int
FME_RG_3D_CONVERT_TO_WIREFRAME: int
FME_RG_RASTER_CONVERT_TO_POLYGON: int
FME_RG_3D_CONVERT_TO_POLYGON: int
FME_RG_3D_REMOVE_VERTICAL_SEGMENTS: int
FME_RG_3D_CONVERT_VERTICAL_FACES_TO_WIREFRAME: int
FME_RG_3D_CONVERT_TO_FACE: int
FME_RG_REMOVE_NULLS: int
FME_RG_3D_AUTO_FRONT_SIDED_SURFACE: int
FME_RG_BISECT_CLOSED_ARCS: int

class FMEGeometryTools:
    """FME Geometry Tools Class

    This class provides the ability to modify FME Geometry."""

    def __init__(self) -> None: ...
    def appendCurve(
        self, destinationCurve: FMECurve or None, sourceCurve: FMECurve or None
    ) -> FMECurve or None:
        """Appends the source curve to the destination curve.

        This will not merge curves but simply append them into an IFMEPath if
        necessary. If the source curve is None, nothing will be done and the
        destination curve will be returned. If the destination curve is None,
        it will be set to the source curve. If the source and destination curves
        do not have touching end points, a line will be inserted to connect them.

        Args:
            destinationCurve (FMECurve or None): The destination curve.
            sourceCurve (FMECurve or None): The source curve.

        Returns:
            (FMECurve or None): The appended curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a
                FMEPath is returned if the geometry truly is a path.
        """
    def applyTransformationToTextureCoordinates(
        self, surface: FMESurface, applyOnlyIfShearExists: bool
    ) -> None:
        """Apply the transformation matrix of the texture to the texture coordinates
        if exists and that it does not have any shear if 'applyOnlyIfShearExists' is set to true.

        Note: This method should only be called once for one surface, or else the
        transformation matrix is applied as many times as the method is called.

        Args:
            surface (FMESurface): The surface.
            applyOnlyIfShearExists (bool): If true, the transformation is only
                applied if the surface has a shear.
        """
    def calculateVertexNormal(
        self, repairOnlyMissing: bool, repairType: int, geom: FMEGeometry
    ) -> None:
        """This method returns None if vertex normals are repaired on the geometry
        or if there is nothing to repair.

        If an error occurs during the repair a FMEException is thrown. Currently,
        the only valid value for repairOnlyMissing is true, and the only valid
        value for repairType is BY_FACE.

        Args:
            repairOnlyMissing (bool): Boolean indicating whether or not to repair
                only the missing vertex normals, currently, the only true is valid.
            repairType (int): Repair type, the only valid value is BY_FACE.
            geom (FMEGeometry):  The geometry to calculate the vertex normals for.
        """
    def closeArcAsEllipse(self, arc: FMEArc) -> FMEEllipse or None:
        """This routine is to see if the current arc is closed.

        A closed arc is defined as one where the start and end points are equal.
        If None is passed in, nothing will be done. The returned geometry may or
        may not be the original object that was passed in. If a different object
        is returned, the original object will be destroyed.

        Args:
            arc (FMEArc): The arc to close.

        Returns:
            (FMEEllipse or None): The Arc closed as an ellipse or None
        """
    def closeCurve(self, curve: FMECurve or None) -> FMECurve or None:
        """This checks to see if the current curve is closed. A closed curve is
        defined as one where the start and end points are equal. If necessary
        this method will add a straight segment from the end point to the start
        point to force the curve closed. If None is passed in, nothing will be
        done and None will be returned. The returned geometry may or may not be
        the original object that was passed in. If a different object is returned,
        the original object will be destroyed.

        Args:
            curve (FMECurve): The curve to close.

        Returns:
            (FMECurve or None): The closed curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMEArc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def closeCurve3D(self, curve: FMECurve or None, mode: int) -> FMECurve or None:
        """This function closes the curve in 3D if it is not already closed.

        If the curve is not 3D, it forces the curve to be 3D with default z value
        of 0.0. A closed curve is defined as one where the start and end points
        are equal in all X, Y and Z coordinates. The returned geometry may or may
        not be the original object that was passed in. If None is passed in,
        nothing will be done and None will be returned. If a different object is
        returned, the original object will be destroyed. There are 3 modes that
        the function uses in deciding how to close the curve, namely
        FME_CLOSE_3D_EXTEND_MODE, FME_CLOSE_3D_AVERAGE_MODE and
        FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        - In FME_CLOSE_3D_AVERAGE_MODE, the curve is closed by modifying the current
        start and end points of the curve to be the average of the two points.
        - In FME_CLOSE_3D_EXTEND_MODE, this method will add a straight segment
        from the end point to the start point to force the curve closed.
        - In FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE, the curve is closed using
        the AVERAGE mode if the start and end points only differ in Z. Otherwise,
        the EXTEND MODE is used.

        Args:
            curve (FMECurve): The curve to close.
            mode (int): The FME_CloseCurve3DMode.

        Returns:
            (FMECurve or None): The closed curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMEPath
                is returned if the geometry truly is a path.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertToLine(self, curve: FMECurve or None) -> FMELine or None:
        """Returns a line that is created from the given curve.

        If the curve is a FMELine, it will be returned. If it is a FMEArc, it will
        be stroked to a line. If the curve is a FMEPath, all segments will be
        returned as their line representations. If the given curve is None, nothing
        will be done. This throws an exception if there is an error.

        Args:
            curve (FMECurve): The curve to convert.

        Returns:
            (FMELine or None): The line representing the curve.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def createXMLFromGeometry(self, geom: FMEGeometry) -> str:
        """This routine returns an XML definition according to the geometry passed in.

        Args:
            geom (FMEGeometry): The geometry to create the XML definition from.

        Returns:
            (str): The geometry definition.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToCurve(
        self, destinationCurve: FMECurve or None, sourceCurve: FMECurve or None
    ) -> FMECurve or None:
        """Extends the source curve to the destination curve.

        If one curve is a line or a path with a line at its end, and the other
        curve is a line or a path with a line at its start, the matching lines
        will be merged, as long as both share the same geometry attributes. If
        the curves do not have touching end points, a line will be created to
        attach them. Appending an arc or appending to an arc will result in a
        path. If the source curve is None, nothing will be done and None will be
        returned. If the destination curve is None, it will be set to the source
        curve.

        Args:
            destinationCurve (FMECurve): The curve to extend with source curve.
            sourceCurve (FMECurve): The curve to extend the destination curve by.

        Returns:
            (FMECurve or None): The extended curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMEPath
                is returned if the geometry truly is a path.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPoint(
        self, curve: FMECurve or None, point: FMEPoint or None
    ) -> FMECurve or None:
        """This method will extend the given curve to the given point.

        This method will add a straight segment from the curve's end point to the
        new point. The returned geometry may or may not be the original object
        that was passed in. If a different object is returned, the original object
        will be destroyed. If the point is None, nothing will be done and None
        will be returned. If the curve is None, but the point is valid, a line
        will be returned that has one point.

        Args:
            curve (FMECurve): The curve to extend with the point or None.
            point (FMEPoint): The point to extend the curve by, or None.

        Returns:
            (FMECurve or None): The extended curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMELine
                is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extractTextLocation(self, text: FMEText) -> FMEGeometry:
        """This routine consumes the text passed in and returns the IFMEGeometry
        that was its location.

        Args:
            text (FMEText): The text to extract the location from.

        Returns:
            (FMEGeometry): The geometry at the text's location. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one of
                the leaf classes in the FMEGeometry inheritance graph. For example,
                a FMELine is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def force2D(self, geometry: FMEGeometry) -> FMEGeometry:
        """This routine forces the geometry to 2D.

        If the geometry is surface or solid, it will become 2D polygons, or
        wire-frame if the surface is vertical.

        Args:
            geometry (FMEGeometry): The geometry to force to 2D.

        Returns:
            (FMEGeometry or None): The geometry in 2D. Note: This method returns
                a terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMELine is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPartCount(
        self,
        geometry: FMEGeometry,
        recursive: bool,
        splitDonuts: bool,
        splitPaths: bool,
    ) -> int:
        """Return the number of parts in the geometry. For multis and aggregates,
        this is the number of parts, and for paths, the number of segments;
        otherwise it is one. If recursive is True, then aggregates' parts will
        be counted recursively.

        Args:
            geometry (FMEGeometry): aggregate or multis whose parts to count.
            recursive (bool): Boolean indicating whether or not to count recursively.
            splitDonuts (bool): Boolean indicating whether or not to split donuts.
            splitPaths (bool): Boolean indictaing whether or to split paths.

        Returns:
            (int): The number of parts in the geometry.
        """
    def join(
        self, firstGeom: FMEGeometry, secondGeom: FMEGeometry, aggregatable: bool
    ) -> FMEGeometry:
        """This routine joins two geometries together.

        Options applying to joining will affect the result. Both geometries will
        be taken ownership if the result is successful. If the joining of two
        geometries doesn't make any sense, put them into an aggregate. For example:
        one ellipse and one line

        Args:
            firstGeom (FMEGeometry): The first geometry to join.
            secondGeom (FMEGeometry): The second geometry to join.
            aggregatable (bool): Boolean indictaing whether or not to combine the
                two geometries into an aggregate.

        Returns:
            (FMEGeometry): The combined geometries. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMELine is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def makeDonuts(self, multiArea: FMEMultiArea) -> FMEGeometry:
        """This routine takes in a MultiArea, extracts simple areas from it, and
        creates donuts out of them. The resulting donuts and simple areas, if any,
        are returned. The returned MultiArea may contain a mixture of donuts and
        simple areas.

        Args:
            multiArea (FMEMultiArea): The multi area to make a donut from.

        Returns:
            (FMEGeometry): The donuts and simple areas extracted form the multi
                area. Note: This method returns a terminal geometry type of the
                FMEGeometry; i.e. one of the leaf classes in the FMEGeometry
                inheritance graph. For example, a FMESimpleArea is returned if
                the geometry truly is a simple area.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def matrixTransform(
        self,
        geometry: FMEGeometry,
        m11: float,
        m12: float,
        m13: float,
        m14: float,
        m21: float,
        m22: float,
        m23: float,
        m24: float,
        m31: float,
        m32: float,
        m33: float,
        m34: float,
    ) -> FMEGeometry:
        """This method performs a 3D matrix transformation on the geometry passed in.

        The order in which parameters are passed in is important and it should be
        row wise e.g. for a matrix the order of the parameters should be m11, m12,
        m13, m14, m21, m22, m23, m24, m31, m32, m33, m34.

        |m11 m12 m13 m14|

        |m21 m22 m23 m24|

        |m31 m32 m33 m34|

        After doing the transformation, geometry is replaced with the transformed
        geometry if the method is successful. Otherwise, the matrix transform has
        failed and a FMEException is thrown.

        Args:
            geometry (FMEGeometry): The geometry to transform.

        Returns:
            (FMEGeometry): The transformed geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMEAggregate is returned if the geometry truly is a aggregate.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def offset(self, geometry: FMEGeometry, point: FMEPoint) -> FMEGeometry:
        """Offsets the geometry by the coords specified by 'point'.

        The returned geometry may or may not be the original object that was
        passed in. If a different object is returned, the original object will
        be destroyed.

        Args:
            geometry (FMEGeometry): The geometry to offset.
            point (FMEPoint): The point specifying the offset distance.

        Returns:
            (FMEGeometry): The offset geometry. Note: This method returns a terminal
                geometry type of the FMEGeometry; i.e. one of the leaf classes in
                the FMEGeometry inheritance graph. For example, a FMELine is
                returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def refineArea(self, area: FMEArea, refineType: int) -> FMEArea:
        """See the documentation for refineGeometry().

        Bitmask elements are defined in Refine Area Type.

        Args:
            area (FMEArea): The area to refine.
            refineType (int): One of: FME_RA_PATH_CONCAT_LINES,
                FME_RA_PATH_EXTRACT_SINGLE_LINES, FME_RA_PATH_EXTRACT_SINGLE_ARCS,
                FME_RA_ARC_STANDARDIZE, FME_RA_ARC_STROKE, FME_RA_AREA_STANDARDIZE,
                FME_RA_LINE_REMOVE_DUPLICATE_COORDS, or FME_RA_LINE_REMOVE_DUPLICATE_COORDS_Z.

        Returns:
            (FMEArea): The refined area. Note: This method returns a terminal
                geometry type of the FMEArea; i.e. one of the leaf classes in the
                FMEArea inheritance graph. For example, a FMEPolygon is returned
                if the geometry truly is a polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def refineCurve(self, curve: FMECurve, refineType: int) -> FMECurve:
        """See the documentation for refineGeometry().

        Bitmask elements are defined in Refine Curve Type.

        Args:
            curve (FMECurve): The curve to refine.
            refineType (int): One of: FME_RC_PATH_CONCAT_LINES,
                FME_RC_PATH_EXTRACT_SINGLE_LINES, FME_RC_PATH_EXTRACT_SINGLE_ARCS,
                FME_RC_ARC_STANDARDIZE, FME_RC_ARC_STROKE,
                FME_RC_LINE_REMOVE_DUPLICATE_COORDS, or FME_RC_LINE_REMOVE_DUPLICATE_COORDS_Z.

        Returns:
            (FMECurve): The refined curve. Note: This method returns a terminal
                geometry type of the FMECurve; i.e. one of the leaf classes in
                the FMECurve inheritance graph. For example, a FMELine is returned
                if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def refineGeometry(self, geometry: FMEGeometry, refineType: int) -> FMEGeometry:
        """This routine offers a number of options to refine geometries.

        The options are defined as a bitmask whose components are defined in
        Refine Geometry Type. Options applying to curves will affect area boundaries.

        - FME_RG_AGG_CONVERT_HOMOGENEOUS_TO_MULTI: Any aggregates that could be
        represented as multis will have their parts removed and a new multi
        will be the result.
        - FME_RG_AGG_OR_MULTI_RECURSE: Elements of aggregates and multis will also
        be refined according to the same parameters.
        - FME_RG_AGG_OR_MULTI_EXTRACT_SINGLETONS: Aggregates or multis with only
        one element will have it removed and returned.
        - FME_RG_AREA_STANDARDIZE: Donuts with no holes will become polygons or
        ellipses, and polygons with arc boundaries will become ellipses.
        - FME_RG_ARC_STROKE: Arcs will be converted to lines.
        - FME_RG_ARC_STANDARDIZE: Center-point arcs will have their parameters
        adjusted so that start angle is in [0, 360) and rotation is in [0, 90].
        - FME_RG_PATH_EXTRACT_SINGLE_ARCS: Paths containing one arc (or other
        non-line segment) and no lines will be replaced by that segment.
        - FME_RG_PATH_EXTRACT_SINGLE_LINES: Paths containing one line and no arcs
        will be replaced by that line.
        - FME_RG_PATH_CONCAT_LINES: Consecutive line parts in a path will be
        combined into single lines, as long as they contain identical geometry
        attributes.
        - FME_RG_LINE_REMOVE_DUPLICATE_COORDS: Consecutive duplicate coordinates
        are removed. Arcs are unmodified. Only x and y values in the coordinates
        are used to detect duplicates.
        - FME_RG_LINE_REMOVE_DUPLICATE_COORDS_Z: Consecutive duplicate coordinates
        are removed. Arcs are unmodified. x, y, and z values in the coordinates
        are used to detect duplicates.
        - FME_RG_3D_CONVERT_TO_WIREFRAME: 3D surfaces and solids will be converted
        into wire-frames.
        - FME_RG_RASTER_CONVERT_TO_POLYGON: Rasters will be replaced with their
        polygon boundaries.
        - FME_RG_3D_CONVERT_TO_POLYGON: 3D surfaces and solids will be converted
        into areas.
        - FME_RG_3D_CONVERT_TO_FACE: 3D surfaces and solids will be converted into
        faces.
        - FME_RG_3D_REMOVE_VERTICAL_SEGMENTS: Any vertical segments that exist in
        three dimensional curves.
        - FME_RG_3D_CONVERT_VERTICAL_FACES_TO_WIREFRAME: Convert any vertical
        faces that exist in 3D surfaces and solids to wire-frames.
        - FME_RG_REMOVE_NULLS: recursively deletes any FMENull geometries.
        Container geometries such as aggregates will become empty if all they
        contained was FMENull. If the user passes in a FMENull, a FMENull will
        be returned.
        - FME_RG_3D_AUTO_FRONT_SIDED_SURFACE: will modify a surface so that it
        is front-sided, where the side selected favors the side with a non-default
        appearance or in the case of two non-default appearances, the side with
        a texture reference.
        - FME_RG_BISECT_CLOSED_ARCS

        Args:
            geometry (FMEGeometry): The geometry to refine.
            refineType (int): One of the Refine Geometry Types.

        Returns:
            (FMEGeometry): The refined geometry. Note: This method returns a terminal
                geometry type of the FMEGeometry; i.e. one of the leaf classes in
                the FMEGeometry inheritance graph. For example, a FMEPolygon is
                returned if the geometry truly is a polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def rotate2D(
        self, geometry: FMEGeometry, center: FMEPoint, angle: float
    ) -> FMEGeometry:
        """The angle is CCW up from the horizontal and is measured in degrees.

        The returned geometry may or may not be the original object that was
        passed in. If a different object is returned, the original object will
        e destroyed. If an error occurs an exception is thrown.

        Args:
            geometry (FMEGeometry): The geometry to rotate.
            center (FMEPoint): The center point.
            angle (float): The angle in degrees.

        Returns:
            (FMEGeometry): The rotated geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMESimpleArea is returned if the geometry truly is a simple area.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(
        self, geometry: FMEGeometry, xScale: float, yScale: float, zScale: float
    ) -> FMEGeometry:
        """The 'zscale' is ignored if geometry is 2D.

        The returned geometry may or may not be the original object that was
        passed in. If a different object is returned, the original object will
        be destroyed. If an error occurs an exception is thrown.

        Args:
            geometry (FMEGeometry): The geometry to scale.
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.

        Returns:
            (FMEGeometry): The scaled geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMESimpleArea is returned if the geometry truly is a simple area.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcPrimaryRadius(self, arc: FMEArc, radius: float) -> FMEArc:
        """Sets the primary radius of an arc.

        Args:
            arc (FMECurve): The arc.
            radius (float): The radius.

        Returns:
            (FMEArc): The arc after the primary radius is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcRotation(self, arc: FMEArc, rotation: float) -> FMEArc:
        """Set the rotation on an arc object.

        All angles are CCW up from the horizontal and are measured in degrees.
        If the underlying arc is stored by bulge or by 3 points, it will become
        an arc by center point.

        Args:
            arc (FMECurve): The arc to set the rotation for.
            rotation (float): The rotation.

        Returns:
            (FMEArc): The arc after the rotation is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcSecondaryRadius(self, arc: FMEArc, radius: float) -> FMEArc:
        """Sets the secondary radius of an arc.

        Args:
            arc (FMECurve): The arc.
            radius (float): The radius.

        Returns:
            (FMEArc): The arc after the secondary radius is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcSweepAngle(self, arc: FMEArc, angle: float) -> FMEArc:
        """Sets the sweep angle of an arc.

         If the angle is a bulge arc, it is turned as an arc by center point to
         support sweep angle of 360.

        Args:
            arc (FMECurve): The arc.
            angle (float): The angle.

        Returns:
            (FMEArc): The arc after the sweep angle is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def splitDoubleSidedSurface(
        self, doubleSidedSurface: FMESurface
    ) -> list[FMESurface]:
        """Takes a double-sided surface and splits it up into two single-sided
        surfaces of the same type.

        If the passed in geometry is actually single-sided, then None is returned
        for the side that doesn't exist. An error is returned when the function
        encounters a problem trying to split up the surface.

        Args:
            doubleSidedSurface (FMESurface): The double-sided surface.

        Returns:
            (List[FMESurface]): A List of the front and back side of doubleSidedSurface,
                in the form [frontSideSurface, backSideSurface].

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def triangulateToSurface(self, geometry: FMEGeometry) -> FMEGeometry:
        """This routine will return a FMEGeometry object with triangle faces.

        This feature can support all geometries except for FMEAggregate,
        FMECSGSolid, FMECompositeSolid and FMEMultiSolid. The output FMEGeometry
        is never None. The resulting FMEGeometry is not guaranteed to contain
        only triangles, so it is the user's responsiblity to check this. The
        geometry type of the returned FMEGeometry object depends on the type of
        input geometry:

        - If the input is a FMETriangleStrip, FMETriangleFan, or FMEFace that is
        already triangular, the resulting FMEGeometry is a copy of the input
        geometry and hence has the same geometry type as the input.
        - If the input is a sliver face, the resulting FMEGeometry is a copy of
        the original geometry.
        - If the input is a non-triangular and non-sliver Face, non-triangular
        Area, or RectangleFace, the resulting FMEGeometry is a FMECompositeSurface,
        whose components are triangular Faces. Otherwise the component is a
        FMECompositeSurface consisting of triangular Faces.
        - If the input is a CompositeSurface, the resulting FMEGeometry is a
        FMECompositeSurface. The type of each component in the resulting
        FMECompositeSurface is determined as described above.
        - If the input is a MultiSurface, the resulting FMEGeometry is a
        FMEMultiSurface. The type of each component in the resulting FMEMultiSurface
        is determined as described above.
        - If the input is a Box, Extrusion, or BRepSolid, the resulting FMEGeometry
        is a FMEBRepSolid.
        - If the input is a MultiArea, the resulting IFMEGeometry is a FMEMultiSurface.
        The type of each component in the resulting FMEMultiSurface is determined
        as described above.
        - If the input is a Mesh, the resulting FMEGeometry is a FMEMultiSurface.
        - For the case of FMEArea, the triangulation will occur with respect to
        the x- and y-coordinates, the z values are ignored, yet they will be
        retained in the output. If there are any errors an exception will be thrown.

        Args:
            geometry (FMEGeometry): The geometry to convert.

        Returns:
            (FMEGeometry): The converted geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMETriangleStrip is returned if the geometry truly is a triangle strip.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMELogFile:
    """FME Log File Class"""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def activityMessage(self, message: str) -> None:
        """[DEPRECATED] Log an activity message to the logfile.

        Args:
            message (str): This is the message string.
        """
    def allowDuplicateMessages(self, allowDuplicateMessages: bool) -> None:
        """This routine sets the allow duplicate messages status of the logfile.

        If in duplicate message mode subsequent messages with the same text are
        logged, otherwise only the first message is logged and the duplicates
        are counted and a count is logged as the next line instead once a
        different message is logged.

        Args:
            allowDuplicateMessages (bool): When True, duplicate messages are not
                hidden in the log. Otherwise if False, log hiding of duplicate
                messages is enabled. Default is False.
        """
    def getAllowDuplicateMessages(self) -> bool:
        """This routine gets the allow duplicate messages status of the logfile.

        If in duplicate message mode subsequent messages with the same text are
        logged, otherwise only the first message is logged and the duplicates
        are counted and a count is logged as the next line instead once a
        different message is logged.

        Returns:
            (bool): Default is False.
        """
    def getFileName(self) -> str:
        """Get the name of the file that is currently being used to log messages.

        Returns:
            (str): Filename
        """
    def getHeldMessages(self) -> bool:
        """Retrieve any held messages and clear the held messages buffer.

        Returns:
            (bool): True if there were held messages, otherwise False.
        """
    def getMessage(
        self, messageNumber: int, messageParameters: list[string_types]  # type: ignore
    ) -> text_type:
        """This method returns the message mapped from 'messageNumber' in
        FME_HOME/messages/fmemessages.fms.

        The mapped message has all its %s replaced by the value in
        'messageParameters' indexed at s, where s is an integer >= 0.

        Args:
            messageNumber (int): The index of the message in FME's 'messages'.
            messageParameters (list[six.string_types]): The values used to
                replace the %s patterns in the returned message, where s is an
                integer >= 0.

        Returns:
            (six.text_type): The mapped message with %s patterns replaced.

        Raises:
            FMEException: An exception is raised if a message is not successfully
            retrieved.
        """
    def getSilent(self) -> bool:
        """Get the silent status of the logfile.

        Returns:
            (bool): Default is False.
        """
    def holdMessages(self, holdMessages: bool) -> None:
        """Inform FME whether or not log messages should be held.

        If set to True, then any log messages will be stored in an internal
        memory buffer for later retrieval, and no messages will be written to
        the log file, or sent to the callback.

        Held messages are retained until they are retrieved with
        getHeldMessages, even if holdMessages is set to False.

        Args:
            holdMessages (bool): If set to True, then any log messages will be
                stored in an internal memory buffer for later retrieval, and no
                messages will be written to the log file, or sent to the callback.
        """
    def logException(self, exception: Exception, severity: int) -> None:
        """Log an exception to the logfile.

        Args:
            exception (Exception): Exception to be logged.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
    def logFeature(self, feature: FMEFeature, severity: int, maxCoords: int) -> None:
        """Log a feature to the logfile.

        Args:
            feature (FMEFeature): The feature is not modified.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
            maxCoords (int): (Optional) Default value: 20. Control how many
                coordinates to output. A value of -1 means all coordinates will
                be output.
        """
    def logMessage(
        self, messageNumber: int, parameters: list[string_types], severity: int  # type: ignore
    ) -> None:
        """Log a message to the logfile.

        Args:
            messageNumber (int): This is the message index, which is stored in a
                file in FME's 'messages' directory.
            parameters (list[six.string_types]): Supply the values for the
                fill-in parameters (0, 1, 2, …) of the message.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
    def logMessageString(self, message: str, severity: int) -> None:
        """Log a simple string to the log file.

        Args:
            message (str): This is the message string.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
    def numFeaturesLogged(self) -> int:
        """Return the total number of features logged.

        Returns:
            (int): The number of features logged.
        """
    def setCallback(self, function: function) -> None:
        """Provide FME with a callback function that will be called whenever a
        message is logged.

        By default, messages will be logged to both the callback function and
        the Log file. If setFileName is called with None as the filename
        parameter, then messages will only be sent to the callback.

        The callback function must take two arguments: An int severity, and a
        string message.

        Args:
            function (Callable): The function to provide FME for use as a
                callback function.
        """
    def setFilename(self, fileName: str, append: bool) -> None:
        """If the filename is different from the current file, then the current
        file is closed, and the new one is opened.

        Args:
            fileName (str): The file name to set.
            append (bool): Append new messages to the file if True. Clear the
                file before any new log messages are added if False.

        Raises:
            FMEException: An exception is raised if there was a problem.
        """
    def silent(self, silent: bool) -> None:
        """Set the 'silent' status of the logfile.

        When in 'silent' mode, nothing is logged.

        Args:
            silent (bool): If set to True, then no messages will be logged.
        """

class FMEException:
    """FME Exception Class

    FME will raise an exception of this type if it encounters an error.

    Attributes:
        message (int or str): The message number defined in a message file, or a
            literal string to use as the error message.
        parms (list[str]):  (Optional) Parameters to the message string. Used
            only if msgNum is used for 'message'. Not to be used if 'message' is
            a string.
    """

    msgNum: int
    def __init__(self, message: int or str, parms: list[str]) -> None:
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            message (int or str): The message number or string to use.
            parms (list[str]): The parameters to use for the message.
        """
        """Initialize self. See help(type(self)) for accurate signature."""
    def with_traceback(self, tb: TracebackType) -> None:
        """set self.__traceback__ to tb and return self."""

# Severity levels
FME_INFORM: int
FME_WARN: int
FME_ERROR: int
FME_FATAL: int
FME_STATISTIC: int
FME_STATUSREPORT: int

# Interpolations
FME_INTERPOLATION_AVERAGE16: int
FME_INTERPOLATION_AVERAGE4: int
FME_INTERPOLATION_BICUBIC: int
FME_INTERPOLATION_BILINEAR: int
FME_INTERPOLATION_NEARESTNEIGHBOR: int
FME_INTERPOLATION_SOURCE: int

# Interpretations
FME_INTERPRETATION_ALPHA16: int
FME_INTERPRETATION_ALPHA8: int
FME_INTERPRETATION_BLUE16: int
FME_INTERPRETATION_BLUE8: int
FME_INTERPRETATION_GRAY16: int
FME_INTERPRETATION_GRAY8: int
FME_INTERPRETATION_GREEN16: int
FME_INTERPRETATION_GREEN8: int
FME_INTERPRETATION_INT16: int
FME_INTERPRETATION_INT32: int
FME_INTERPRETATION_INT64: int
FME_INTERPRETATION_INT8: int
FME_INTERPRETATION_NULL: int
FME_INTERPRETATION_REAL32: int
FME_INTERPRETATION_REAL64: int
FME_INTERPRETATION_RED16: int
FME_INTERPRETATION_RED8: int
FME_INTERPRETATION_RGB24: int
FME_INTERPRETATION_RGB48: int
FME_INTERPRETATION_RGBA32: int
FME_INTERPRETATION_RGBA64: int
FME_INTERPRETATION_STRING: int
FME_INTERPRETATION_UINT16: int
FME_INTERPRETATION_UINT32: int
FME_INTERPRETATION_UINT64: int
FME_INTERPRETATION_UINT8: int

# Reinterpretation modes
FME_REINTERPRET_MODE_BAND: int
FME_REINTERPRET_MODE_PALETTE: int
FME_REINTERPRET_MODE_RASTER: int

# Cell resize operations
FME_CELL_RESIZE_PRESERVE_CELL_SHAPE: int
FME_CELL_RESIZE_PRESERVE_NUM_CELLS: int
FME_CELL_RESIZE_SQUARE_CELLS: int

# Calculate Aspect parameters
kFME_CalculateAspect_interpolateNodata: int
kFME_CalculateAspect_algorithm: int
kFME_CalculateAspect_algorithm_Horn: int
kFME_CalculateAspect_algorithm_ZevenbergenThorne: int

# Calculate Slope parameters
kFME_CalculateSlope_interpolateNodata: int
kFME_CalculateSlope_algorithm: int
kFME_CalculateSlope_algorithm_Horn: int
kFME_CalculateSlope_algorithm_ZevenbergenThorne: int

# Interpretation conversion parameters
kFME_ConvertInterpretation_RGBAToRGB: int
kFME_ConvertInterpretation_RGBAToRGB_applyAlpha: int
kFME_ConvertInterpretation_RGBAToRGB_dropAlpha: int
kFME_ConvertInterpretation_RGBToRGBA: int
kFME_ConvertInterpretation_RGBToRGBA_createAlphaFromNodata: int
kFME_ConvertInterpretation_RGBToRGBA_createOpaqueAlpha: int
kFME_ConvertInterpretation_colorNumeric_boundedCast: int
kFME_ConvertInterpretation_colorNumeric_cast: int
kFME_ConvertInterpretation_colorNumeric_dataScale: int
kFME_ConvertInterpretation_colorNumeric_typeScale: int
kFME_ConvertInterpretation_colorToColor: int
kFME_ConvertInterpretation_colorToNumeric: int
kFME_ConvertInterpretation_floatToInteger: int
kFME_ConvertInterpretation_floatToInteger_ceil: int
kFME_ConvertInterpretation_floatToInteger_floor: int
kFME_ConvertInterpretation_floatToInteger_round: int
kFME_ConvertInterpretation_manyToOneBand: int
kFME_ConvertInterpretation_manyToOneBand_average: int
kFME_ConvertInterpretation_numericToColor: int
kFME_ConvertInterpretation_numericToNumeric: int

# Hillshade parameters
kFME_Hillshade_algorithm: int
kFME_Hillshade_algorithm_Horn: int
kFME_Hillshade_algorithm_ZevenbergenThorne: int
kFME_Hillshade_interpolateNodata: int

# Mosaicking parameters
kFME_Mosaic_mergePalettes: int
kFME_Mosaic_nodataOverwrite: int
kFME_Mosaic_overlappingValues: int
kFME_Mosaic_overlappingValues_average: int
kFME_Mosaic_overlappingValues_compositeUsingAlpha: int
kFME_Mosaic_overlappingValues_last: int
kFME_Mosaic_overlappingValues_max: int
kFME_Mosaic_overlappingValues_min: int
kFME_Mosaic_overlappingValues_sum: int

# Nodata mask parameters
kFME_CreateNodataMask_removeNodata: int

# Clip parameters
kFME_Clip_preserveExtents: int

# Resampling parameters
kFME_Resample_snapOffsetX: int
kFME_Resample_snapOffsetY: int

# Scaling parameters
kFME_RasterScale_scaleSpacingOnly: int

# Slope Type Units
FME_SLOPETYPE_DEGREES: int
FME_SLOPETYPE_PERCENTRISE: int

class FMERasterTools:
    pass

class FMEBandTilePopulator:
    pass

# FMEReader.setConstraints() keywords

kFMERead_AllFeatures: int
kFMERead_EnvelopeHeightInPixels: int
kFMERead_EnvelopeIntersects: int
kFMERead_EnvelopeWidthInPixels: int
kFMERead_FMEType: int
kFMERead_FeatureType: int
kFMERead_Geometry: int
kFMERead_SearchType: int
kFMERead_Where: int

# FMESpatialIndex directives
kFME_SIPassphrase: int
kFME_SISerializeRasterData: int

# Has Support For Constants (support_type)
FME_SUPPORT_FEATURE_TABLE: int
FME_SUPPORT_FEATURE_TABLE_SHIM: int
FME_SUPPORT_FEATURE_TABLES_ONLY: int
FME_SUPPORT_WRITER_GET_SCHEMA: int

class FMEDialog:
    """FME Dialog Class

    Provides access to the standard FME dialog boxes."""

    def about(self, applicationName: str) -> None:
        """This method displays a dialog box that shows the kind of FME license
        and FME build number that the FMEObjects application is using.

        Args:
            applicationName (str): The name of the application.
        """
    def coordSysPrompt(self, coordSysName: str) -> str or None:
        """This method displays a standard FME coordinate system dialog to prompt
        the user to choose a coordinate system.

        Args:
            coordSysName (str): (Optional) the default coordinate system to be
                highlighted when the dialog is opened.

        Returns:
            (str): The coordinate system name chosen by the user.
        """
    def destPrompt(
        self,
        defaultDestFormat: str,
        defaultDestDataset: str,
        userDirectives: dict[str, str] or list[str],
    ) -> tuple[str, str, list[str]] or None:
        """This method displays a dialog to prompt the user to choose a destination
        format and dataset.

        Args:
            defaultDestFormat (str): The default format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultDestDataset (str): The default dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            userDirectives (dict[str,str] or list[str]): (Optional) Specify one
                or more additional directives to be used by the dialog. All elements
                in this collection must be strings. A list should be used if one
                key is to be set to multiple values. If a list is passed in,
                key-value pairs such as those in a dict must be placed side by
                side. For example, the key should be placed in the first list
                element, followed by the value for the key.
                These user directives are honoured:
                TITLE: The title to be used in the dialog box.
                - LIMIT_FORMATS: The short names of the only formats that will
                be allowed, separated by | characters.
                - EXCLUDE_FORMATS: The short names of the formats that will NOT
                be allowed, separated by | characters. Exclude takes precedence
                over LIMIT_FORMATS.
                - SETTINGS_ONLY: If value is “yes”, then the settings box is shown
                for the passed in default destination format/dataset The default
                is “no”.
                - SPATIAL_SETTINGS If value is “yes”, then any settings box that
                allows for specifying spatial constraints will have that aspect
                remain enabled. The default is”yes”. If the value is “no”, then
                the spatial area specification aspect of the settings boxes is
                disabled. This directive is useful for disabling spatial settings
                when a source dialog is done only for the purpose of gathering
                schema information.

        Returns:
            (str, str, list[str]): The destination format and dataset along with
                the user directives, these can be used directly with the
                FMEUniversalWriter. This tuple is formatted (destFormat,
                destDataset, [directives]). None is returned if the user pressed
                Cancel. The directives returned are as follows:

                - RUNTIME_MACROS: The runtime macros are in the next position.
                - META_MACROS: The metafile macros are in the next position.
                - METAFILE: The metafile name is in the next position.
                - COORDSYS: The coordinate system is in the next position.
        """
    def featTypeProperties(
        self, format: str, source: bool, schemaFeat: FMEFeature
    ) -> FMEFeature or None:
        """Bring up the feature type properties dialog on the given schema feature.

        Args:
            format (str): The format name for the format this schema feature is a part of.
            source (bool):  True if this feature type is a source, False otherwise.
            schemaFeat (FMEFeature): The schema feature to edit. The schema feature is represented through the following values on the feature:

            - Feature Type: The feature type of the schema feature.
            - Geometry Type: The geometry type(s) of the schema feature, set as
            the 'fme_geometry{n}' attribute on the schema feature, where n is an
            index starting at 0. The geometry type values are the format specific
            geometry types that are defined in the metafile of the target format.
            - User Attributes: The user attribute(s) of the schema feature, set
            as regular attribute name/type pairs on the schema feature.
            - Format Attributes: The format attribute(s) of the schema feature,
            set as 'fme_format_attr_name{n}' and 'fme_format_attr_type{n}'
            attributes on the schema feature, where n is an index starting at 0.

        Returns:
            (FMEFeature): The schema feature that has been edited, None otherwise.
        """
    def generate(self, defaultSourceDataset: str) -> tuple[str, str]:
        """This method displays the Generate Workspace dialog box.

        Args:
            defaultSourceDataset (str): The default source dataset displayed in
                the Generate Workspace dialog.

        Returns:
            tuple[str, str]: The parameter filename and workspace filename. This
                tuple is formatted: (parameterFileName, workspaceFileName).
                Returns None if the user hit cancel.The parameterFileName that is
                returned can be used to generate a workspace with this fme
                invocation:fme PARAMETER_FILE < parameterFile > Then the parameterFile
                should be deleted from the disk. The workspace itself will not
                exist until after the FME returns.
        """
    def guessFormat(self, filename: str) -> str or None:
        """This method attempts to guess the format based on the extension of the filename passed in.

        Args:
            filename (str): The filename to be used to guess the format.

        Returns:
            (str): The format guessed or None if we were unable to make a guess.
        """
    def parameterPrompt(self, filename: str) -> bool:
        """This method parses the file with the passed in name and does a standard
        FME dialog for the parameters listed in the GUI lines in the file.

        If any DEFAULT_MACRO lines were found, these supply default values. If
        the user exits the form with OK, then the file will be overwritten with
        a new file that alternates MACRO NAME and VALUE, line by line.

        Args:
            filename (str): The name of the file to be parsed.

        Returns:
            bool: True if the user pressed OK, False otherwise.
        """
    def sourcePrompt(
        self,
        defaultSourceFormat: str,
        defaultSourceDataset: str,
        userDirectives: dict[str, str] or list[str],
    ) -> tuple[str, str, list[str]] or None:
        """This method displays a dialog to prompt the user to choose a source format and dataset.

        Args:
            defaultSourceFormat (str): The default format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultSourceDataset (str): The default dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            userDirectives (dict[str,str] or list[str]): (Optional) Specify one
                or more additional directives to be used by the dialog. All elements
                in this collection must be strings. A list should be used if one
                key is to be set to multiple values. If a list is passed in,
                key-value pairs such as those in a dict must be placed side by
                side. For example, the key should be placed in the first list
                element, followed by the value for the key.
                These user directives are honoured:
                TITLE: The title to be used in the dialog box.
                - LIMIT_FORMATS: The short names of the only formats that will
                be allowed, separated by | characters.
                - EXCLUDE_FORMATS: The short names of the formats that will NOT
                be allowed, separated by | characters. Exclude takes precedence
                over LIMIT_FORMATS.
                - SETTINGS_ONLY: If value is “yes”, then the settings box is shown
                for the passed in default source format/dataset The default
                is “no”.
                - SPATIAL_SETTINGS If value is “yes”, then any settings box that
                allows for specifying spatial constraints will have that aspect
                remain enabled. The default is”yes”. If the value is “no”, then
                the spatial area specification aspect of the settings boxes is
                disabled. This directive is useful for disabling spatial settings
                when a source dialog is done only for the purpose of gathering
                schema information.

        Returns:
            (str, str, list[str]): The source format and dataset along with the
                user directives, these can be used directly with the FMEUniversalReader.
                This tuple is formated (sourceFormat, sourceDataset, [directives]).
                None is returned if the user pressed Cancel. The directives returned
                are as follows:

                - RUNTIME_MACROS: The runtime macros are in the next position.
                - META_MACROS: The metafile macros are in the next position.
                - METAFILE: The metafile name is in the next position.
                - COORDSYS: The coordinate system is in the next position.
                - IDLIST: The id list is in the next position.
        """
    def xlatePrompt(
        self,
        defaultSourceFormat: str,
        defaultSourceDataset: str,
        defaultDestFormat: str,
        defaultDestDataset: str,
        userDirectives: dict[str, str] or list[str],
    ) -> tuple[str, str, str, str, list[str]] or None:
        """This method displays a dialog to prompt the user to choose a source format, dataset, destination format and dataset.

        Args:
            defaultSourceFormat (str): The default format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultSourceDataset (str): The default dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultDestFormat (str): The default destination format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultDestDataset (str): The default destination dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            userDirectives (dict[str,str] or list[str]): (Optional) Specify one
                or more additional directives to be used by the dialog. All elements
                in this collection must be strings. A list should be used if one
                key is to be set to multiple values. If a list is passed in,
                key-value pairs such as those in a dict must be placed side by
                side. For example, the key should be placed in the first list
                element, followed by the value for the key.
                These user directives are honoured:
                TITLE: The title to be used in the dialog box.
                - LIMIT_FORMATS: The short names of the only formats that will
                be allowed, separated by | characters.
                - EXCLUDE_FORMATS: The short names of the formats that will NOT
                be allowed, separated by | characters. Exclude takes precedence
                over LIMIT_FORMATS.
                - SETTINGS_ONLY: If value is “yes”, then the settings box is shown
                for the passed in default source format/dataset The default
                is “no”.
                - SPATIAL_SETTINGS If value is “yes”, then any settings box that
                allows for specifying spatial constraints will have that aspect
                remain enabled. The default is”yes”If the value is “no”, then the
                spatial area specification aspect of the settings boxes is disabled.
                This directive is useful for disabling spatial settings when a
                source dialog is done only for the purpose of gathering schema
                information.

          Returns:
              (str, str, str, str, list[str]): The source format, source dataset,
              destination format, and destination dataset along with the source
              user directives and destination user directives, these can be used
              directly with the FMEUniversalReader and FMEUniversalWriter respectively.
              This tuple is formated (sourceFormat, sourceDataset, destFormat,
              destDataset, [sourceUserDirectives], [destUserDirectives]). None is
              returned if the user pressed Cancel. The source user directives
              returned are as follows:

              - RUNTIME_MACROS: The runtime macros are in the next position.
              - META_MACROS: The metafile macros are in the next position.
              - METAFILE: The metafile name is in the next position.
              - COORDSYS: The coordinate system is in the next position.
              - IDLIST: The id list is in the next position.

              The destination user directives returned are as follows:`
              - RUNTIME_MACROS: The runtime macros are in the next position.
              - META_MACROS: The metafile macros are in the next position.
              - METAFILE: The metafile name is in the next position.
              - COORDSYS: The coordinate system is in the next position.
        """

class FMEFactoryPipeline:
    """FME Factory Pipeline Class"""

class FMERegex:
    """FME Regex Class"""

    def __init__(self, regexPattern: text_type) -> None:
        """This class provides FME regular expression functionality that is
        differs from Python's built-in re module.

        Returns: (FMERegex): The FMERegex object.
        """
    def findall(self, inputString: text_type) -> list[text_type]:
        """Return all non-overlapping matches in string, as a list of strings.

        The string is scanned left-to-right, and matches are returned in the
        order found.

        Args:
            inputString (text_type): The string to search.

        Returns: (list[text_type]): The list of matches.
        """
    def findlist(self, inputString: text_type) -> list[text_type]:
        """Return a list yielding match objects over all non-overlapping matches in string.

        The string is scanned left-to-right, and matches are returned in the order
        found.

        Args:
            inputString (text_type): The string to search.

        Returns: (list[text_type]): A list of match tuples of the form (match,
            start, end), where match is the string segment matching the regular
            expression pattern, start is the start index of the string segment,
            and end is the end index of the string segment.
        """
    def match(self, inputString: text_type) -> tuple[str, int, int]:
        """If zero or more characters at the beginning of string match this regular
        expression, return a corresponding match tuple.

        Args:
            inputString (text_type): The string to search.

        Returns: (tuple[str, int, int]): A match tuple of the form
            (match, start, end), where match is the string segment matching the
            regular expression pattern, start is the start index of the string
            segment, and end is the end index of the string segment. None is
            returned if a match is not found.
        """
    def search(self, inputString: str) -> tuple[str, int, int]:
        """Scan through string looking for the first location where this regular
        expression produces a match, and return a corresponding match object.

        Args:
            inputString (str): The string to search.

        Returns: (tuple[str, int, int]): A match tuple of the form
            (match, start, end), where match is the string segment matching the
            regular expression pattern, start is the start index of the string
            segment, and end is the end index of the string segment. None is
            returned if a match is not found.
        """

class FMESession:
    """FME Session Class"""

class FMESpatialIndex:
    """FME Spatial Index Class"""

class FMETemporaryFileManager:
    """FME Temporary File Manager Class"""

class FMEUniversalReader:
    """FME Universal Reader Class"""

class FMEUniversalWriter:
    """FME Universal Writer Class"""

class FMEWorkspaceRunner:
    """FME Workspace Runner Class"""
