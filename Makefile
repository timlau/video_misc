VERSION = 0.1
SHOTCUT_DATA=/home/tim/Documents/Shotcut

update-presets:
	@rm -rf Shotcut
	python ./create_grid_presets/create_grid_presets.py 2 2 -o ./Shotcut/Grid_2x2/1080/
	python ./create_grid_presets/create_grid_presets.py 2 3 -o ./Shotcut/Grid_2x3/1080/
	python ./create_grid_presets/create_grid_presets.py 3 3 -o ./Shotcut/Grid_3x3/1080/

update-shocut:
	@rm -f $(SHOTCUT_DATA)/presets/cropRectangle/Grid*
	python ./create_grid_presets/create_grid_presets.py 3 3 -o $(SHOTCUT_DATA)


release:
	@git tag -f -m "Added ${VERSION} release tag" ${VERSION}
	@git push --tags origin
	@rm -f *.zip
	zip -r shotcut_presets_grid_2x2.zip /Shotcut/Grid_2x2
	zip -r shotcut_presets_grid_2x3.zip /Shotcut/Grid_2x3
	zip -r shotcut_presets_grid_3x3.zip /Shotcut/Grid_3x3