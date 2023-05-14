VERSION = 0.2
SHOTCUT_DATA=/home/tim/Documents/Shotcut

update-presets:
	@rm -rf Shotcut
	python ./create_grid_presets/create_grid_presets.py 2 2 -o ./Shotcut/Grid_2x2/1080/
	python ./create_grid_presets/create_grid_presets.py 2 3 -o ./Shotcut/Grid_2x3/1080/
	python ./create_grid_presets/create_grid_presets.py 3 3 -o ./Shotcut/Grid_3x3/1080/
	python ./create_grid_presets/create_slidein_presets.py 3 3 --size 2 -o ./Shotcut/SlideIn/3x3_2/1080_30FPS/

update-shocut:
	@rm -f $(SHOTCUT_DATA)/presets/cropRectangle/Grid*
	python ./create_grid_presets/create_grid_presets.py 3 3 -o $(SHOTCUT_DATA)
	@rm -f $(SHOTCUT_DATA)/presets/cropRectangle/SlideIn*
	python ./create_grid_presets/create_slidein_presets.py 3 3 --size 2 -o $(SHOTCUT_DATA)

zip-release:
	@rm -f shotcut_presets*.zip
	zip -r shotcut_presets_grid_2x2.zip ./Shotcut/Grid_2x2
	zip -r shotcut_presets_grid_2x3.zip ./Shotcut/Grid_2x3
	zip -r shotcut_presets_grid_3x3.zip ./Shotcut/Grid_3x3
	zip -r shotcut_presets_slidein_3x3_2.zip ./Shotcut/Grid_3x3

release:
	@git commit -a -m "release ${VERSION}"
	@git tag -f -m "Added ${VERSION} release tag" release-${VERSION}
	@git push
	@git push --tags origin
	@$(MAKE) zip-release