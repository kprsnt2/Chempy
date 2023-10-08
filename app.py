import streamlit as st
from chempy import Substance
from chempy.search import PubChem

# Streamlit app title
st.title("Chemical Formula Info Lookup")

# User input for chemical formula
formula_input = st.text_input("Enter a chemical formula (e.g., H2O):")

if formula_input:
    try:
        # Create a Substance object from the user's input
        substance = Substance.from_formula(formula_input)

        # Display basic information about the substance
        st.write("Formula:", substance.formula)
        st.write("Molar mass:", substance.mass)

        # Search for more information about the substance on PubChem
        search_results = PubChem.search(substance)

        if search_results:
            result = search_results[0]  # Take the first search result
            st.write("\nAdditional information from PubChem:")
            st.write("Common name:", result.common_name)
            st.write("IUPAC name:", result.iupac_name)
            st.write("Molecular weight:", result.molecular_weight)
            st.write("CAS Registry Number:", result.cas)

        else:
            st.warning("No information found on PubChem for this formula.")

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Add a link to PubChem for more details
st.markdown("[More details on PubChem](https://pubchem.ncbi.nlm.nih.gov/)")

# This line allows the Streamlit app to run in the browser
if __name__ == "__main__":
    st.set_page_config(page_title="Chemical Formula Info Lookup")
