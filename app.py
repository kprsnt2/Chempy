import streamlit as st
import pubchempy as pcp

# Streamlit app title and description
st.title("Chemical Formula Info Lookup")
st.write("Enter a chemical formula to learn more about it!")

# User input for chemical formula
formula_input = st.text_input("Enter a chemical formula (e.g., H2O):")

if formula_input:
    try:
        # Search for compounds with the given formula on PubChem
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
            st.warning("No information found on PubChem for this formula.")

    except Exception as e:
        st.error(f"Error: {str(e)}")

    # Add a "Reset" button to clear the input field
    st.button("Reset")
