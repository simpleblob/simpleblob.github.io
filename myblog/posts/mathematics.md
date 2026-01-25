---

title: Mathematics
subtitle: None
description: None
tags: math
created: 2018-01-02
published: 2018-12-02
status: draft
confidence: log
importance: 1
---
## Linear Algebra (Matrix/Vector)

[3brown1blue videos playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

### Basis Vectors

Think of a vector as an arrow pointing on a map, with origin at [0,0]. Basis vectors i and j represent each x and y coordinate on the map.

### Linear Transformation

Linear transformation is like squishing or enlarging nD dimensional space. The transformation is only linear if the origin stays fixed and spacing remains equal.

**Key properties:**

- We put the new basis vector as column 1, 2, etc. of the transformation matrix. We use the dot product to apply the transformation.
- A 2x3 transformation matrix means we are squishing from 3D to 2D coordinates.
- Order matters. "Rotate then shear" is not the same as "shear then rotate."
- Transformations are associative. You can compute the product of transformations (called compositions) as long as they are in the right order.
### Determinant

The determinant is the area or volume change caused by the basis vectors of a matrix. It shows whether the transformation expands or squishes space.

When the determinant is zero, we lose a dimension. This is why we might not have an inverse matrix.

### Inverse Matrix

Think of doing the transformation in reverse. That's how we find the inverse matrix.

When the determinant is zero, we effectively lose a dimension, which means many possible inverses exist.

### Cross Product

In two dimensions, the cross product between two vectors produces:

- A unit vector orthogonal to both input vectors (direction depends on right-hand order)
- Scaled by the determinant (area) of the two input vectors

### Change of Basis

Let A be a vector in basis₁, and B be a transformation matrix in basis₂.

We can construct a change of basis vector Q for basis₁ → basis₂. Then we make the transformation matrix C = inv_Q * B * Q. Finally, we apply to A, getting Â = C * A in basis₁.

### Eigenvectors and Eigenvalues

**Eigenvectors** are the orthogonal vectors that don't change direction after some transformation Q.

**Eigenvalues** are the scaling values (lengthen or shorten) associated with certain eigenvectors.

**Why this matters:** We can use eigenvectors to change basis, then make transformation products much easier to calculate. We only need scaling transformations, which means diagonal matrices.
