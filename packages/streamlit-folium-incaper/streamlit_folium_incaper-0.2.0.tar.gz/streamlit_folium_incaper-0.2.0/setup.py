import setuptools

setuptools.setup(
    name="streamlit_folium_incaper",
    version="0.2.0",
    author="Henrique Dalmagro",
    author_email="henriquedalmagro04@gmail.com",
    description="Render Folium objects in Streamlit for INCAPER",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/Xdeivison/streamlit-foliumx",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=["streamlit>=1.13.0", "folium>=0.13,!=0.15.0", "jinja2", "branca"],
)
