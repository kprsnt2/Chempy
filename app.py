import streamlit as st
import pubchempy as pcp

# Streamlit app title and description
st.title("Chemical Formula Info Lookup")
st.write("Enter a chemical formula to learn more about it!")

# User input for chemical formula
formula_input = st.text_input("Enter a chemical formula (e.g., H2O):")

if formula_input:
    try:
        # Try searching for compounds with the given formula using the 'formula' query type
        compounds = pcp.get_compounds(formula_input, 'formula')

        if compounds:
            compound = compounds[0]  # Take the first search result

            # Display basic information about the compound
            st.subheader("Basic Information:")
            st.write(f"- Formula: {compound.molecular_formula}")
            st.write(f"- Molecular Weight: {compound.molecular_weight:.2f} g/mol")

            # Display more information (you can add more details as needed)
            st.subheader("Additional Information:")
            st.write(f"- IUPAC Name: {compound.iupac_name}")
            st.write(f"- Synonyms: {', '.join(compound.synonyms)}")

        else:
            # If no compounds are found, retry with a different query type ('name')
            name_compounds = pcp.get_compounds(formula_input, 'name')

            if name_compounds:
                compound = name_compounds[0]  # Take the first search result
                st.subheader("Basic Information:")
                st.write(f"- Formula: {compound.molecular_formula}")
                st.write(f"- Molecular Weight: {compound.molecular_weight:.2f} g/mol")
                st.subheader("Additional Information:")
                st.write(f"- IUPAC Name: {compound.iupac_name}")
                st.write(f"- Synonyms: {', '.join(compound.synonyms)}")
            else:
                st.warning("No information found on PubChem for this formula.")

    except Exception as e:
        st.error(f"Error: {str(e)}")

    # Add a "Reset" button to clear the input field
    st.button("Reset")
