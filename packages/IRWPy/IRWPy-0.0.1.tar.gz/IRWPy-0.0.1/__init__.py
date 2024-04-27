def inverse_radius_weighting(x, y, E, values, xi, yi, power=2, neighbors=12):
    """
    Inverse Radius Weighting (IRW) interpolation.
    
    Parameters:
    - x, y: Arrays of measured point coordinates.
    - E: Array of elevations corresponding to the points.
    - values: Array of measured values corresponding to the points.
    - xi, yi: Coordinates of the location where interpolation is needed.
    - power: Exponent for the distance weights.
    
    Returns:
    - Interpolated value at (xi, yi).
    """

    distances = np.sqrt((x - xi)**2 + (y - yi)**2)

    ## Check for and remove 0 distance points
    if 0 in distances:
        zero_distance_index = np.where(distances==0)
        tmp_distances = np.delete(distances, zero_distance_index)
        tmp_values = np.delete(values, zero_distance_index)
        tmp_E = np.delete(E, zero_distance_index)
    else:
        tmp_distances = distances
        tmp_values = values
        tmp_E = E
        
    ## For a specific number of neighbors: 1. sort distances asc 2. take top n (shortest) distances
    if neighbors == "all":
        asc_values = tmp_values
        weights = 1.0 / ((tmp_distances**power) + (tmp_E**power))
    else:
        asc_values = [x for _, x in sorted(zip(tmp_distances, tmp_values))][0:neighbors]
        tmp_E = [x for _, x in sorted(zip(tmp_distances, tmp_E))][0:neighbors]
        distances_asc = np.asarray(sorted(tmp_distances)[0:neighbors])
        
        weights = 1.0 / ((distances_asc**power) + (np.asarray(tmp_E)**power))

    
    weighted_values = asc_values * weights
    interpolated_value = np.sum(weighted_values) / np.sum(weights)
    
    return interpolated_value