""" The hmesh module provides an halfedge based mesh representation. 
In addition this module contains a variety of functions for mesh manipulation and inspection.
Specifcally, the module contains functions for mesh simplification, smoothing, subdivision, 
and editing of vertices, faces, and edges. The volumetric_isocontour function allows us to 
create a polygonal mesh from volumetric data by isocontouring. The skeleton_to_feq function 
allows us to turn a skeleton graph into a Face Extrusion Quad Mesh.
"""
import ctypes as ct
import numpy as np
from math import sqrt
from numpy import ndarray
from numpy.linalg import norm
from pygel3d import lib_py_gel, IntVector, Vec3dVector, spatial
from scipy.sparse import csc_matrix, vstack
from scipy.sparse.linalg import lsqr
from collections import defaultdict


class Manifold:
    """ The Manifold class represents a halfedge based mesh. It is maybe a bit grand to call
    a mesh class Manifold, but meshes based on the halfedge representation are manifold (if we
    ignore a few corner cases) unlike some other representations. This class contains a number of
    methods for mesh manipulation and inspection. Note also that numerous further functions are
    available to manipulate meshes stored as Manifolds.

    Many of the functions below accept arguments called hid, fid, or vid. These are simply indices
    of halfedges, faces and vertices, respectively: integer numbers that identify the corresponding
    mesh element. Using a plain integer to identify a mesh entity means that, for instance, a
    vertex index can also be used as an index into, say, a NumPy array without any conversion.
    """
    def __init__(self,orig=None):
        if orig == None:
            self.obj = lib_py_gel.Manifold_new()
        else:
            self.obj = lib_py_gel.Manifold_copy(orig.obj)
    @classmethod
    def from_triangles(cls,vertices, faces):
        """ Given a list of vertices and triangles (faces), this function produces
        a Manifold mesh."""
        m = cls()
        vertices = np.asarray(vertices,dtype=np.float64, order='C')
        faces = np.asarray(faces,dtype=ct.c_int, order='C')
        m.obj = lib_py_gel.Manifold_from_triangles(len(vertices),len(faces),vertices,faces)
        return m
    @classmethod
    def from_points(cls,pts,xaxis=np.array([1,0,0]),yaxis=np.array([0,1,0])):
        """ This function computes the Delaunay triangulation of pts. You need
        to specify xaxis and yaxis if they are not canonical. The function returns
        a Manifold with the resulting triangles. Clearly, this function will
        give surprising results if the surface represented by the points is not
        well represented as a 2.5D surface, aka a height field. """
        m = cls()
        pts = np.asarray(pts,dtype=np.float64, order='C')
        xaxis = np.asarray(xaxis,dtype=np.float64, order='C')
        yaxis = np.asarray(yaxis,dtype=np.float64, order='C')
        m.obj = lib_py_gel.Manifold_from_points(len(pts), pts, xaxis, yaxis)
        return m
    def __del__(self):
        lib_py_gel.Manifold_delete(self.obj)
    def merge_with(self, other):
        """ Merge this Manifold with another one given as the argument. This function
        does not return anything. It simply combines the two meshes in the Manifold on which
        the method is called. """
        lib_py_gel.Manifold_merge(self.obj, other.obj)
    def add_face(self,pts):
        """ Add a face to the Manifold.
        This function takes a list of 3D points, pts, as argument and creates a face
        in the mesh with those points as vertices. The function returns the index
        of the created face.
        """
        pts = np.asarray(pts,dtype=np.float64, order='C')
        return lib_py_gel.Manifold_add_face(self.obj, len(pts), pts)
    def positions(self):
        """ Retrieve an array containing the vertex positions of the Manifold.
        It is not a copy: any changes are made to the actual vertex positions. """
        pos = ct.POINTER(ct.c_double)()
        n = lib_py_gel.Manifold_positions(self.obj, ct.byref(pos))
        return np.ctypeslib.as_array(pos,(n,3))
    def no_allocated_vertices(self):
        """ Number of vertices.
        This number could be higher than the number of actually
        used vertices, but corresponds to the size of the array allocated
        for vertices."""
        return lib_py_gel.Manifold_no_allocated_vertices(self.obj)
    def no_allocated_faces(self):
        """ Number of faces.
        This number could be higher than the number of actually
        used faces, but corresponds to the size of the array allocated
        for faces."""
        return lib_py_gel.Manifold_no_allocated_faces(self.obj)
    def no_allocated_halfedges(self):
        """ Number of halfedges.
        This number could be higher than the number of actually
        used halfedges, but corresponds to the size of the array allocated
        for halfedges."""
        return lib_py_gel.Manifold_no_allocated_halfedges(self.obj)
    def vertices(self):
        """ Returns an iterable containing all vertex indices"""
        verts = IntVector()
        n = lib_py_gel.Manifold_vertices(self.obj, verts.obj)
        return verts
    def faces(self):
        """ Returns an iterable containing all face indices"""
        faces = IntVector()
        n = lib_py_gel.Manifold_faces(self.obj, faces.obj)
        return faces
    def halfedges(self):
        """ Returns an iterable containing all halfedge indices"""
        hedges = IntVector()
        n = lib_py_gel.Manifold_halfedges(self.obj, hedges.obj)
        return hedges
    def circulate_vertex(self, vid, mode='v'):
        """ Circulate a vertex. Passed a vertex index, vid, and second argument,
        mode='f', this function will return an iterable with all faces incident
        on vid arranged in counter clockwise order. Similarly, if mode is 'h',
        incident halfedges (outgoing) are returned, and for mode = 'v', all
        neighboring vertices are returned. """
        nbrs = IntVector()
        n = lib_py_gel.Manifold_circulate_vertex(self.obj, vid, ct.c_char(mode.encode('ascii')), nbrs.obj)
        return nbrs
    def circulate_face(self, fid, mode='v'):
        """ Circulate a face. Passed a face index, fid, and second argument,
        mode='f', this function will return an iterable with all faces that
        share an edge with fid (in counter clockwise order). If the argument is
        mode='h', the halfedges themselves are returned. For mode='v', the
        incident vertices of the face are returned. """
        nbrs = IntVector()
        n = lib_py_gel.Manifold_circulate_face(self.obj, fid, ct.c_char(mode.encode('ascii')), nbrs.obj)
        return nbrs
    def next_halfedge(self,hid):
        """ Returns next halfedge to hid. """
        return lib_py_gel.Walker_next_halfedge(self.obj, hid)
    def prev_halfedge(self,hid):
        """ Returns previous halfedge to hid. """
        return lib_py_gel.Walker_prev_halfedge(self.obj, hid)
    def opposite_halfedge(self,hid):
        """ Returns opposite halfedge to hid. """
        return lib_py_gel.Walker_opposite_halfedge(self.obj, hid)
    def incident_face(self,hid):
        """ Returns face corresponding to hid. """
        return lib_py_gel.Walker_incident_face(self.obj, hid)
    def incident_vertex(self,hid):
        """ Returns vertex corresponding to (or pointed to by) hid. """
        return lib_py_gel.Walker_incident_vertex(self.obj, hid)
    def remove_vertex(self,vid):
        """ Remove vertex vid from the Manifold. This function merges all faces
        around the vertex into one and then removes this resulting face. """
        return lib_py_gel.Manifold_remove_vertex(self.obj, vid)
    def remove_face(self,fid):
        """ Removes a face, fid, from the Manifold. If it is an interior face it is
        simply replaced by an invalid index. If the face contains boundary
        edges, these are removed. Situations may arise where the mesh is no
        longer manifold because the situation at a boundary vertex is not
        homeomorphic to a half disk. This, we can probably ignore since from the
        data structure point of view it is not really a problem that a vertex is
        incident on two holes - a hole can be seen as a special type of face.
        The function returns false if the index of the face is not valid,
        otherwise the function must complete. """
        return lib_py_gel.Manifold_remove_face(self.obj, fid)
    def remove_edge(self,hid):
        """ Remove an edge, hid, from the Manifold. This function will remove the
        faces on either side and the edge itself in the process. Thus, it is a
        simple application of remove_face. """
        return lib_py_gel.Manifold_remove_edge(self.obj, hid)
    def vertex_in_use(self,vid):
        """ check if vertex, vid, is in use. This function returns true if the id corresponds
        to a vertex that is currently in the mesh and false otherwise. vid could
        be outside the range of used ids and it could also correspond to a vertex
        which is not active. The function returns false in both cases. """
        return lib_py_gel.Manifold_vertex_in_use(self.obj, vid)
    def face_in_use(self,fid):
        """ check if face, fid, is in use. This function returns true if the id corresponds
        to a face that is currently in the mesh and false otherwise. fid could
        be outside the range of used ids and it could also correspond to a face
        which is not active. The function returns false in both cases. """
        return lib_py_gel.Manifold_face_in_use(self.obj, fid)
    def halfedge_in_use(self,hid):
        """ check if halfedge hid is in use. This function returns true if the id corresponds
        to a halfedge that is currently in the mesh and false otherwise. hid could
        be outside the range of used ids and it could also correspond to a halfedge
        which is not active. The function returns false in both cases. """
        return lib_py_gel.Manifold_halfedge_in_use(self.obj, hid)
    def flip_edge(self,hid):
        """ Flip the edge, hid, separating two faces. The function first verifies that
        the edge is flippable. This entails making sure that all of the
        following are true.
        1. adjacent faces are triangles.
        2. neither end point has valency three or less.
        3. the vertices that will be connected are not already.
        If the tests are passed, the flip is performed and the function
        returns True. Otherwise False."""
        return lib_py_gel.Manifold_flip_edge(self.obj,hid)
    def collapse_edge(self,hid, avg_vertices=False):
        """ Collapse an edge hid.
        Before collapsing hid, a number of tests are made:
        ---
        1.  For the two vertices adjacent to the edge, we generate a list of all their neighbouring vertices.
        We then generate a  list of the vertices that occur in both these lists.
        That is, we find all vertices connected by edges to both endpoints of the edge and store these in a list.
        2.  For both faces incident on the edge, check whether they are triangular.
        If this is the case, the face will be removed, and it is ok that the the third vertex is connected to both endpoints.
        Thus the third vertex in such a face is removed from the list generated in 1.
        3.  If the list is now empty, all is well.
        Otherwise, there would be a vertex in the new mesh with two edges connecting it to the same vertex. Return false.
        4.  TETRAHEDRON TEST:
        If the valency of both vertices is three, and the incident faces are triangles, we also disallow the operation.
        Reason: A vertex valency of two and two triangles incident on the adjacent vertices makes the construction collapse.
        5.  VALENCY 4 TEST:
        If a triangle is adjacent to the edge being collapsed, it disappears.
        This means the valency of the remaining edge vertex is decreased by one.
        A valency two vertex reduced to a valency one vertex is considered illegal.
        6.  PREVENT MERGING HOLES:
        Collapsing an edge with boundary endpoints and valid faces results in the creation where two holes meet.
        A non manifold situation. We could relax this...
        7. New test: if the same face is in the one-ring of both vertices but not adjacent to the common edge,
        then the result of a collapse would be a one ring where the same face occurs twice. This is disallowed as the resulting
        face would be non-simple.
        If the tests are passed, the collapse is performed and the function
        returns True. Otherwise False."""
        return lib_py_gel.Manifold_collapse_edge(self.obj, hid, avg_vertices)
    def split_face_by_edge(self,fid,v0,v1):
        """   Split a face. The face, fid, is split by creating an edge with
        endpoints v0 and v1 (the next two arguments). The vertices of the old
        face between v0 and v1 (in counter clockwise order) continue to belong
        to fid. The vertices between v1 and v0 belong to the new face. A handle to
        the new face is returned. """
        return lib_py_gel.Manifold_split_face_by_edge(self.obj, fid, v0, v1)
    def split_face_by_vertex(self,fid):
        """   Split a polygon, fid, by inserting a vertex at the barycenter. This
        function is less likely to create flipped triangles than the
        split_face_triangulate function. On the other hand, it introduces more
        vertices and probably makes the triangles more acute. The vertex id of the
        inserted vertex is returned. """
        return lib_py_gel.Manifold_split_face_by_vertex(self.obj,fid)
    def split_edge(self,hid):
        """   Insert a new vertex on halfedge hid. The new halfedge is insterted
        as the previous edge to hid. The vertex id of the inserted vertex is returned. """
        return lib_py_gel.Manifold_split_edge(self.obj,hid)
    def stitch_boundary_edges(self,h0,h1):
        """   Stitch two halfedges. Two boundary halfedges, h0 and h1, can be stitched
        together. This can be used to build a complex mesh from a bunch of
        simple faces. """
        return lib_py_gel.Manifold_stitch_boundary_edges(self.obj, h0, h1)
    def merge_faces(self,hid):
        """   Merges two faces into a single polygon. The merged faces are those shared
        by the edge for which hid is one of the two corresponding halfedges. This function returns
        true if the merging was possible and false otherwise. Currently merge
        only fails if the mesh is already illegal. Thus it should, in fact,
        never fail. """
        if self.is_halfedge_at_boundary(hid):
            return False
        fid = self.incident_face(hid)
        return lib_py_gel.Manifold_merge_faces(self.obj, fid, hid)
    def close_hole(self,hid):
        """ Close hole given by hid (i.e. the face referenced by hid). Returns
        index of the created face or the face that was already there if, in
        fact, hid was not next to a hole. """
        return lib_py_gel.Manifold_close_hole(self.obj, hid)
    def cleanup(self):
        """ Remove unused items from Mesh. This function remaps all vertices, halfedges
        and faces such that the arrays do not contain any holes left by unused mesh
        entities. It is a good idea to call this function when a mesh has been simplified
        or changed in other ways such that mesh entities have been removed. However, note
        that it invalidates any attributes that you might have stored in auxilliary arrays."""
        lib_py_gel.Manifold_cleanup(self.obj)
    def is_halfedge_at_boundary(self, hid):
        """ Returns True if hid is a boundary halfedge, i.e. face on either
        side is invalid. """
        return lib_py_gel.is_halfedge_at_boundary(self.obj, hid)
    def is_vertex_at_boundary(self, vid):
        """ Returns True if vid lies on a boundary. """
        return lib_py_gel.is_vertex_at_boundary(self.obj, vid)
    def edge_length(self, hid):
        """ Returns length of edge given by halfedge hid which is passed as argument. """
        return lib_py_gel.length(self.obj, hid)
    def valency(self,vid):
        """ Returns valency of vid, i.e. number of incident edges."""
        return lib_py_gel.valency(self.obj,vid)
    def vertex_normal(self, vid):
        """ Returns vertex normal (angle weighted) of vertex given by vid """
        n = ndarray(3,dtype=np.float64)
        lib_py_gel.vertex_normal(self.obj, vid, n)
        return n
    def connected(self, v0, v1):
        """ Returns true if the two argument vertices, v0 and v1, are in each other's one-rings."""
        return lib_py_gel.connected(self.obj,v0,v1)
    def no_edges(self, fid):
        """ Compute the number of edges of a face fid """
        return lib_py_gel.no_edges(self.obj, fid)
    def face_normal(self, fid):
        """ Compute the normal of a face fid. If the face is not a triangle,
        the normal is not defined, but computed using the first three
        vertices of the face. """
        n = ndarray(3, dtype=np.float64)
        lib_py_gel.face_normal(self.obj, fid, n)
        return n
    def area(self, fid):
        """ Returns the area of a face fid. """
        return lib_py_gel.area(self.obj, fid)
    def perimeter(self, fid):
        """ Returns the perimeter of a face fid. """
        return lib_py_gel.perimeter(self.obj, fid)
    def centre(self, fid):
        """ Returns the centre of a face. """
        c = ndarray(3, dtype=np.float64)
        lib_py_gel.centre(self.obj, fid, c)
        return c

def valid(m):
    """This function performs a series of tests to check that this
    is a valid manifold. This function is not rigorously constructed but seems
    to catch all problems so far. The function returns true if the mesh is valid
    and false otherwise. """
    return lib_py_gel.valid(m.obj)

def closed(m):
    """ Returns true if m is closed, i.e. has no boundary."""
    return lib_py_gel.closed(m.obj)

def bbox(m):
    """ Returns the min and max corners of the bounding box of Manifold m. """
    pmin = ndarray(3,dtype=np.float64)
    pmax = ndarray(3,dtype=np.float64)
    lib_py_gel.bbox(m.obj, pmin, pmax)
    return pmin, pmax

def bsphere(m):
    """ Calculate the bounding sphere of the manifold m.
    Returns centre,radius """
    c = ndarray(3,dtype=np.float64)
    r = (ct.c_double)()
    lib_py_gel.bsphere(m.obj, c, ct.byref(r))
    return (c,r)

def stitch(m, rad=1e-30):
    """ Stitch together edges of m whose endpoints coincide geometrically. This
    function allows you to create a mesh as a bunch of faces and then stitch
    these together to form a coherent whole. What this function adds is a
    spatial data structure to find out which vertices coincide. The return value
    is the number of edges that could not be stitched. Often this is because it
    would introduce a non-manifold situation."""
    return lib_py_gel.stitch_mesh(m.obj,rad)

def obj_save(fn, m):
    """ Save Manifold m to Wavefront obj file. """
    s = ct.c_char_p(fn.encode('utf-8'))
    lib_py_gel.obj_save(s, m.obj)

def off_save(fn, m):
    """ Save Manifold m to OFF file. """
    s = ct.c_char_p(fn.encode('utf-8'))
    lib_py_gel.off_save(s, m.obj)

def x3d_save(fn, m):
    """ Save Manifold m to X3D file. """
    s = ct.c_char_p(fn.encode('utf-8'))
    lib_py_gel.x3d_save(s, m.obj)

def obj_load(fn):
    """ Load and return Manifold from Wavefront obj file.
    Returns None if loading failed. """
    m = Manifold()
    s = ct.c_char_p(fn.encode('utf-8'))
    if lib_py_gel.obj_load(s, m.obj):
        return m
    return None

def off_load(fn):
    """ Load and return Manifold from OFF file.
    Returns None if loading failed."""
    m = Manifold()
    s = ct.c_char_p(fn.encode('utf-8'))
    if lib_py_gel.off_load(s, m.obj):
        return m
    return None

def ply_load(fn):
    """ Load and return Manifold from Stanford PLY file.
    Returns None if loading failed. """
    m = Manifold()
    s = ct.c_char_p(fn.encode('utf-8'))
    if lib_py_gel.ply_load(s, m.obj):
        return m
    return None

def x3d_load(fn):
    """ Load and return Manifold from X3D file.
    Returns None if loading failed."""
    m = Manifold()
    s = ct.c_char_p(fn.encode('utf-8'))
    if lib_py_gel.x3d_load(s, m.obj):
        return m
    return None

from os.path import splitext
def load(fn):
    """ Load a Manifold from an X3D/OBJ/OFF/PLY file. Return the
    loaded Manifold. Returns None if loading failed."""
    name, extension = splitext(fn)
    if extension.lower() == ".x3d":
        return x3d_load(fn)
    if extension.lower() == ".obj":
        return obj_load(fn)
    if extension.lower() == ".off":
        return off_load(fn)
    if extension.lower() == ".ply":
        return ply_load(fn)
    return None

def save(fn, m):
    """ Save a Manifold, m, to an X3D/OBJ/OFF file. """
    name, extension = splitext(fn)
    if extension.lower() == ".x3d":
        x3d_save(fn, m)
    elif extension.lower() == ".obj":
        obj_save(fn, m)
    elif extension.lower() == ".off":
        off_save(fn, m)


def remove_caps(m, thresh=2.9):
    """ Remove caps from a manifold, m, consisting of only triangles. A cap is a
    triangle with two very small angles and an angle close to pi, however a cap
    does not necessarily have a very short edge. Set the ang_thresh to a value
    close to pi. The closer to pi the _less_ sensitive the cap removal. A cap is
    removed by flipping the (long) edge E opposite to the vertex V with the
    angle close to pi. However, the function is more complex. Read code and
    document more carefully !!! """
    lib_py_gel.remove_caps(m.obj,thresh)

def remove_needles(m, thresh=0.05, average_positions=False):
    """  Remove needles from a manifold, m, consisting of only triangles. A needle
    is a triangle with a single very short edge. It is moved by collapsing the
    short edge. The thresh parameter sets the length threshold (in terms of the average edge length
    in the mesh). If average_positions is true then the collapsed vertex is placed at the average position of the end points."""
    abs_thresh = thresh * average_edge_length(m)
    lib_py_gel.remove_needles(m.obj,abs_thresh, average_positions)

def close_holes(m, max_size=100):
    """  This function replaces holes in m by faces. It is really a simple function
    that just finds all loops of edges next to missing faces. """
    lib_py_gel.close_holes(m.obj, max_size)

def flip_orientation(m):
    """  Flip the orientation of a mesh, m. After calling this function, normals
    will point the other way and clockwise becomes counter clockwise """
    lib_py_gel.flip_orientation(m.obj)

def merge_coincident_boundary_vertices(m, rad = 1.0e-30):
    """  Merge vertices of m that are boundary vertices and coincident.
        However, if one belongs to the other's one ring or the one
        rings share a vertex, they will not be merged. """
    lib_py_gel.merge_coincident_boundary_vertices(m.obj, rad)

def minimize_curvature(m,anneal=False):
    """ Minimizes mean curvature of m by flipping edges. Hence, no vertices are moved.
     This is really the same as dihedral angle minimization, except that we weight by edge length. """
    lib_py_gel.minimize_curvature(m.obj, anneal)

def minimize_dihedral_angle(m,max_iter=10000, anneal=False, alpha=False, gamma=4.0):
    """ Minimizes dihedral angles in m by flipping edges.
        Arguments:
        max_iter is the maximum number of iterations for simulated annealing.
        anneal tells us the code whether to apply simulated annealing
        alpha=False means that we use the cosine of angles rather than true angles (faster)
        gamma is the power to which the angles are raised."""
    lib_py_gel.minimize_dihedral_angle(m.obj, max_iter, anneal,alpha,ct.c_double(gamma))


def maximize_min_angle(m,dihedral_thresh=0.95,anneal=False):
    """ Maximizes the minimum angle of triangles by flipping edges of m. Makes the mesh more Delaunay."""
    lib_py_gel.maximize_min_angle(m.obj,dihedral_thresh,anneal)

def optimize_valency(m,anneal=False):
    """ Tries to achieve valence 6 internally and 4 along edges by flipping edges of m. """
    lib_py_gel.optimize_valency(m.obj, anneal)

def randomize_mesh(m,max_iter=1):
    """  Make random flips in m. Useful for generating synthetic test cases. """
    lib_py_gel.randomize_mesh(m.obj, max_iter)

def quadric_simplify(m,keep_fraction,singular_thresh=1e-4,error_thresh=1):
    """ Garland Heckbert simplification of mesh m. keep_fraction is the fraction of vertices
    to retain. The singular_thresh determines how subtle features are preserved. For values
    close to 1 the surface is treated as smooth even in the presence of sharp edges of low
    dihedral angle (angle between normals). Close to zero, the method preserves even subtle
    sharp features better. The error_thresh is the value of the QEM error at which
    simplification stops. It is relative to the bounding box size. The default value is 1
    meaning that simplification continues until the model has been simplified to a number of
    vertices approximately equal to keep_fraction times the original number of vertices."""
    lib_py_gel.quadric_simplify(m.obj, keep_fraction, singular_thresh,error_thresh)

def average_edge_length(m):
    """ Returns the average edge length of mesh m. """
    return lib_py_gel.average_edge_length(m.obj)

def median_edge_length(m):
    """ Returns the median edge length of m"""
    return lib_py_gel.median_edge_length(m.obj)

def refine_edges(m,threshold):
    """ Split all edges in m which are longer
    than the threshold (second arg) length. A split edge
    results in a new vertex of valence two."""
    return lib_py_gel.refine_edges(m.obj, threshold)

def cc_split(m):
    """ Perform a Catmull-Clark split on m, i.e. a split where each face is divided
    into new quadrilateral faces formed by connecting a corner with a point on
    each incident edge and a point at the centre of the face."""
    lib_py_gel.cc_split(m.obj)

def loop_split(m):
    """ Perform a loop split on m where each edge is divided into two segments, and
    four new triangles are created for each original triangle. """
    lib_py_gel.loop_split(m.obj)

def root3_subdivide(m):
    """ Leif Kobbelt's subdivision scheme applied to m. A vertex is placed in the
    center of each face and all old edges are flipped. """
    lib_py_gel.root3_subdivide(m.obj)

def rootCC_subdivide(m):
    """ This subdivision scheme creates a vertex inside each original (quad) face of m,
    producing four triangles. Triangles sharing an old edge are then merged.
    Two steps produce something similar to Catmull-Clark. """
    lib_py_gel.rootCC_subdivide(m.obj)

def butterfly_subdivide(m):
    """ Butterfly subidiviosn on m. An interpolatory scheme. Creates the same connectivity as Loop. """
    lib_py_gel.butterfly_subdivide(m.obj)

def cc_smooth(m):
    """ If called after cc_split, this function completes a step of Catmull-Clark
    subdivision of m."""
    lib_py_gel.cc_smooth(m.obj)

def cc_subdivide(m):
    """ Perform a full Catmull-Clark subdivision step on mesh m. """
    lib_py_gel.cc_split(m.obj)
    lib_py_gel.cc_smooth(m.obj)

def loop_subdivide(m):
    """ Perform a full Loop subdivision step on mesh m. """
    lib_py_gel.loop_split(m.obj)
    lib_py_gel.loop_smooth(m.obj)   

def volume_preserving_cc_smooth(m, iter):
    """ This function does the same type of smoothing as in Catmull-Clark
    subdivision, but to preserve volume it actually performs two steps, and the
    second step is negative as in Taubin smoothing."""
    lib_py_gel.volume_preserving_cc_smooth(m.obj, iter)

def regularize_quads(m, w=0.5, shrink=0.0, iter=1):
    """ This function smooths a quad mesh by regularizing quads. Essentially,
    regularization just makes them more rectangular. """
    lib_py_gel.regularize_quads(m.obj, w, shrink, iter)


def loop_smooth(m):
    """ If called after Loop split, this function completes a step of Loop
    subdivision of m. """
    lib_py_gel.loop_smooth(m.obj)
    
def taubin_smooth(m, iter=1):
    """ This function performs Taubin smoothing on the mesh m for iter number
    of iterations. """
    lib_py_gel.taubin_smooth(m.obj, iter)

def laplacian_smooth(m, w=0.5, iter=1):
    """ This function performs Laplacian smoothing on the mesh m for iter number
    of iterations. w is the weight applied. """
    lib_py_gel.laplacian_smooth(m.obj, w, iter)

def anisotropic_smooth(m, sharpness=0.5, iter=1):
    """ This function performs anisotropic smoothing on the mesh m for iter number
    of iterations. A bilateral filtering controlled by sharpness is performed on 
    the face normals followed by a rotation of the faces to match the new normals.
    The updated vertex positions are the average positions of the corners of the 
    rotated faces. For sharpness==0 the new normal is simply the area weighted 
    average of the normals of incident faces. For sharpness>0 the weight of the
    neighbouring face normals is a Gaussian function of the angle between the
    face normals. The greater the sharpness, the more the smoothing is anisotropic."""
    lib_py_gel.anisotropic_smooth(m.obj, sharpness, iter)
    
def volumetric_isocontour(data, bbox_min = None, bbox_max = None,
                          tau=0.0,
                          make_triangles=True,
                          high_is_inside=True,
                          dual_connectivity=False):
    """ Creates a polygonal mesh from volumetric data by isocontouring. The dimensions
    are given by dims, bbox_min (defaults to [0,0,0] ) and bbox_max (defaults to dims) are
    the corners of the bounding box in R^3 that corresponds to the volumetric grid, tau is
    the iso value (defaults to 0). If make_triangles is True (default), we turn the quads
    into triangles. Finally, high_is_inside=True (default) means that values greater than
    tau are interior and smaller values are exterior. If dual_connectivity is False (default)
    the function produces marching cubes connectivity and if True it produces dual contouring
    connectivity. MC connectivity tends to produce less nice triangle shapes but since the
    vertices always lie on edges, the geometry is arguably better defined for MC. """
    m = Manifold()
    dims = data.shape
    if bbox_min is None:
        bbox_min = (0,0,0)
    if bbox_max is None:
        bbox_max = dims
    data_float = np.asarray(data, dtype=ct.c_float, order='F')
    bbox_min_d = np.asarray(bbox_min, dtype=np.float64, order='C')
    bbox_max_d = np.asarray(bbox_max, dtype=np.float64, order='C')
    lib_py_gel.volumetric_isocontour(m.obj, dims[0], dims[1], dims[2],
                                     data_float, bbox_min_d, bbox_max_d, tau,
                                     make_triangles, high_is_inside, dual_connectivity)
    return m

def triangulate(m, clip_ear=True):
    """ Turn a general polygonal mesh, m, into a triangle mesh by repeatedly
        splitting a polygon into smaller polygons. """
    if clip_ear:
        lib_py_gel.ear_clip_triangulate(m.obj)
    else:
        lib_py_gel.shortest_edge_triangulate(m.obj)

def skeleton_to_feq(g, node_radii = None, symmetrize=True):
    """ Turn a skeleton graph g into a Face Extrusion Quad Mesh m with given node_radii for each graph node.
    If symmetrize is True (default) the graph is made symmetrical. If node_radii are supplied then they
    are used in the reconstruction. Otherwise, the radii are obtained from the skeleton. They are stored in 
    the green channel of the vertex color during skeletonization, so for a skeletonized shape that is how the
    radius of each node is obtained. This is a questionable design decision and will probably change 
    in the future. """
    m = Manifold()
    if node_radii is None:
        node_radii = [0.0] * len(g.nodes())
        use_graph_radii = True
    else:
        use_graph_radii = False
        if isinstance(node_radii, (int, float)):
            if node_radii <= 0.0:
                node_radii = 0.25 * g.average_edge_length()
            node_radii = [node_radii] * len(g.nodes())

    node_rs_flat = np.asarray(node_radii, dtype=np.float64)
    lib_py_gel.graph_to_feq(g.obj , m.obj, node_rs_flat, symmetrize, use_graph_radii)
    return m

# def non_rigid_registration(m, ref_mesh):
#     """ Perform non-rigid registration of m to ref_mesh. """
#     lib_py_gel.non_rigid_registration(m.obj, ref_mesh.obj)

def laplacian_matrix(m):
    num_verts = m.no_allocated_vertices()
    laplacian = np.full((num_verts,num_verts), 0.0)
    for i in m.vertices():
        neighbors = m.circulate_vertex(i)
        deg = len(neighbors)
        laplacian[i][i] = 1.0
        for v in neighbors:
            laplacian[i][v] = -1/deg
    return csc_matrix(laplacian)


def inv_correspondence_leqs(m, ref_mesh):
    m_pos = m.positions()
    ref_pos = ref_mesh.positions()

    m_tree = spatial.I3DTree()
    for v in m.vertices():
        m_tree.insert(m_pos[v],v)
    m_tree.build()

    m_target_pos = np.zeros(m.positions().shape)
    m_cnt = np.zeros(m.no_allocated_vertices())
    for r_id in ref_mesh.vertices():
        query_pt = ref_pos[r_id]
        closest_pt_obj = m_tree.closest_point(query_pt,1e32)
        if closest_pt_obj is not None:
            key,m_id = closest_pt_obj
            r_norm = ref_mesh.vertex_normal(r_id)
            m_norm = m.vertex_normal(m_id)
            dot_prod = m_norm @ r_norm
            if dot_prod > 0.5:
                v = query_pt - m_pos[m_id]
                wgt = dot_prod - 0.5
                m_target_pos[m_id] += wgt*query_pt
                m_cnt[m_id] += wgt
                
    N = m.no_allocated_vertices()
    A_list = []
    b_list = []
    for vid in m.vertices():
        if m_cnt[vid] > 0.0:
            row_a = np.zeros(N)
            row_a[vid] = 1.0
            A_list.append(row_a)
            b_list.append(m_target_pos[vid]/m_cnt[vid])
    return csc_matrix(np.array(A_list)), np.array(b_list)

def fit_mesh_to_ref(m, ref_mesh, iter = 10, dist_wt = 1.0, lap_wt = 0.3):
    """ Fits a skeletal mesh m to a reference mesh ref_mesh. """

    v_pos = m.positions()
    for i in range(iter):
        Ai, bi = inv_correspondence_leqs(m, ref_mesh)
        lap_matrix = laplacian_matrix(m)
        lap_b = lap_matrix @ v_pos
        final_A = vstack([lap_wt*lap_matrix, dist_wt*Ai])
        final_b = np.vstack([lap_wt*lap_b, dist_wt*bi])
        opt_x, _, _, _ = lsqr(final_A, final_b[:,0])[:4]
        opt_y, _, _, _ = lsqr(final_A, final_b[:,1])[:4]
        opt_z, _, _, _ = lsqr(final_A, final_b[:,2])[:4]
        v_pos[:,:] = np.stack([opt_x, opt_y, opt_z], axis=1)
        regularize_quads(m, w=0.5, shrink=0.8, iter=3)
    return m

class MeshDistance:
    """ This class allows you to compute the distance from any point in space to
    a Manifold (which must be triangulated). The constructor creates an instance
    based on a specific mesh, and the signed_distance function computes the actual distance. """
    def __init__(self,m):
        self.obj = lib_py_gel.MeshDistance_new(m.obj)
    def __del__(self):
        lib_py_gel.MeshDistance_delete(self.obj)
    def signed_distance(self,pts,upper=1e30):
        """ Compute the signed distance from each point in pts to the mesh stored in
        this class instance. pts should be convertible to a length N>=1 array of 3D
        points. The function returns an array of N distance values with a single distance
        for each point. The distance corresponding to a point is positive if the point
        is outside and negative if inside. The upper parameter can be used to threshold
        how far away the distance is of interest. """
        p = np.asarray(pts, dtype=ct.c_float, order='C')
        ndim = len(p.shape)
        if ndim==1:
            n = p.shape[0]//3
        elif ndim==2:
            n = p.shape[0]
        else:
            raise Exception("you must pass signed_distance pts as a 1D array or a 2D array of dim nx3")
        
        d = np.ndarray(n, dtype=ct.c_float)
        lib_py_gel.MeshDistance_signed_distance(self.obj, n, p, d, upper)
        return d
    def ray_inside_test(self,pts,no_rays=3):
        """Check whether each point in pts is inside or outside the stored mesh by
        casting rays. pts should be convertible to a length N>=1 array of 3D points.
        Effectively, this is the sign of the distance. In some cases casting (multiple)
        ray is more robust than using the sign computed locally. Returns an array of
        N integers which are either 1 or 0 depending on whether the corresponding point
        is inside (1) or outside (0). """
        p = np.asarray(pts, dtype=ct.c_float, order='C')
        ndim = len(p.shape)
        if ndim==1:
            n = p.shape[0]//3
        elif ndim==2:
            n = p.shape[0]
        else:
            raise Exception("you must pass signed_distance pts as a 1D array or a 2D array of dim nx3")
        s = np.ndarray(n, dtype=ct.c_int)
        lib_py_gel.MeshDistance_ray_inside_test(self.obj,n,p,s,no_rays)
        return s
    def intersect(self, p0, dir, _t=0):
        """ Intersect the ray starting in p0 with direction, dir, with the stored mesh. Returns
        the point of intersection if there is one, otherwise None. """
        p0 = np.asarray(p0,dtype=ct.c_float)
        dir = np.asarray(dir,dtype=ct.c_float)
        t = ct.c_float(_t)
        r = lib_py_gel.MeshDistance_ray_intersect(self.obj, p0, dir, ct.byref(t))
        if r:
            return t.value, p0, dir
        return None
