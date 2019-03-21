# def data_frame_to_tuple(d_frame):
#     """
#     convert a data frame to tuple
#     :param d_frame:
#     :return:
#     """
#     d_frame_subset = d_frame[['COMPANY NAME', 'ST', 'PHONE']]
#     return [tuple(x) for x in d_frame_subset.values]

# def get_non_duplicate_labels():
#     """
#     get labels with no duplicate
#     :return:
#     """
#     non_duplicate_labels = pd.concat(g for _, g in labels.groupby("COMPANY NAME") if len(g) == 1)
#     return non_duplicate_labels


# def get_duplicate_labels():
#     """
#     get labels with duplicates
#     :return:
#     """
#     duplicate_labels = pd.concat(g for _, g in labels.groupby("COMPANY NAME") if len(g) > 1)
#     return duplicate_labels
#
#
# def get_aggregate_duplicate_labels():
#     """
#     group duplicated labels by company name and state(ST)
#     merges the two phone numbers for label with the same name and state
#     :return:
#     """
#     labels_ = get_duplicate_labels()
#     labels_['PHONE'] = labels_.PHONE.astype(str)  # convert phone field to be str instead BigInt
#     a_labels = labels_.groupby(['COMPANY NAME', 'ST']).agg({
#         'PHONE': ','.join
#     }).reset_index()
#
#     return a_labels


# def duplicate_match_labels(d_labels):
#     """
#
#     :param d_labels:
#     :return:
#
#      Algorithm to match and insert duplicates values
#
#      - Get trimmed duplicates value
#      - for each trimmed duplicates value:
#             -  get the occurrences in non_duplicate list
#             -  Use the first occurrence to check If there is match for label name
#             - match found
#                 - update the match value with the contact, country and state of the first occurence value
#                 - There reinsert the other occurrences
#             else:
#                 reinsert all occurrences
#
#
#     """
#     clean_labels = d_labels.iloc[:, [0]]  # get label names
#     s_labels = clean_labels.drop_duplicates()  # drop duplicates
#     with get_db_connection() as con:
#         cur = con.cursor()
#         for _, label in s_labels.iterrows():
#             occurrences = d_labels.loc[d_labels['COMPANY NAME'] == label['COMPANY NAME']]  # get all occurrences
#             l_occurrences = data_frame_to_tuple(occurrences)  # cast data-frames to list of tuples
#             first_occurrence, *other_occurrences = l_occurrences  # unpack first and other occurrences
#             cur.execute(QUERY_TO_MATCH_LABEL_DATA, (label['COMPANY NAME'], label['COMPANY NAME']))
#             matches = cur.fetchall()
#
#             if matches:
#                 _, _, description, image_url, _ = matches[0]
#
#                 print('Update with this occurrence=', first_occurrence)
#                 update_label_data(matches[0], first_occurrence)
#
#                 print('Insert these occurrences=', other_occurrences)
#                 insert_multiple_label_data(other_occurrences, description, image_url)
#             else:
#
#                 print('Insert these occurrences=', l_occurrences)
#                 insert_multiple_label_data(l_occurrences, description=None, image_url=None)
#             print("----------------")
#         # con.commit()
